const LOCATIONS = [
    {title: 'Park Ave Penthouse', location: {lat: 40.7713024, lng: -73.9632393}},
    {title: 'Chelsea Loft', location: {lat: 40.7444883, lng: -73.9949465}},
    {title: 'Union Square Open Floor Plan', location: {lat: 40.7347062, lng: -73.9895759}},
    {title: 'East Village Hip Studio', location: {lat: 40.7281777, lng: -73.984377}},
    {title: 'TriBeCa Artsy Bachelor Pad', location: {lat: 40.7195264, lng: -74.0089934}},
    {title: 'Chinatown Homey Space', location: {lat: 40.7180628, lng: -73.9961237}}
];

var map;
var bounds;
var infoWindow;
const CLIENT_ID = "GDSKZUME2F4FHOX4JTB0RNYFSBUX5XSPZ3T0BP3RPWDI1FPI";
const CLIENT_SECRET = "MTS2HLC04KEVTNJM2NN4NJE2Y5HCER0MQNLXLJ2VBY3VZO4X";

function initMap() {
    map = new google.maps.Map(document.querySelector("#map"), {
        center: {lat: 40.712775, lng: -74.005973},
        zoom: 10,
        mapTypeControl: false
    });

    bounds = new google.maps.LatLngBounds();
    infoWindow = new google.maps.InfoWindow();
    ko.applyBindings(new ViewModel());
};

const Location = function(loc) {
    const self = this;
    this.visible = ko.observable(true);

    this.title = loc.title;
    this.location = loc.location;
    this.marker = new google.maps.Marker({
        position: this.location,
        title: this.title,
        animation: google.maps.Animation.DROP,
    });

    this.marker.addListener("click", function() {
        if (this.animation !== null) {
            this.setAnimation(null);
        }
        
        populateInfoWindow(self, infoWindow);
    });

    this.showMarker = ko.computed(function() {
        self.marker.setMap(null);
        if (self.visible()) {
            self.marker.setMap(map);
            bounds.extend(self.marker.position);
        }
        map.fitBounds(bounds);
    }, this);
};

const ViewModel = function() {
    const self = this;

    this.searchText = ko.observable("");
    // rateLimit'ed to stop from losing focus too quickly before bounce animation can be set off
    this.isSelected = ko.observable(false).extend({ rateLimit: 500});
    this.locations = ko.observableArray();

    LOCATIONS.forEach(function(loc) {
        self.locations.push(new Location(loc));
    });

    this.filterLocations = ko.computed(function(){
        const searchTextLower = self.searchText().toLowerCase();
        // Reset location list visibility
        ko.utils.arrayForEach(self.locations(), function(loc) {
            loc.visible(true);
            callFourSquareVenuesApi(loc);
        });

        // Filter location list and set visibility
        if (self.searchText()) {
            ko.utils.arrayForEach(self.locations(), function(loc) {
                loc.visible(loc.title.toLowerCase().includes(searchTextLower));
            });
        }
        return self.locations();
    }, this);

    this.bounce = function(loc) {
        // Clear all animations
        ko.utils.arrayForEach(self.locations(), function(loc) {
            loc.marker.setAnimation(null);
        });

        loc.marker.setAnimation(google.maps.Animation.BOUNCE);
    };
};

function populateInfoWindow(loc, infowindow) {
    if (infowindow.marker != loc.marker) {
        infowindow.setContent("");
        infowindow.marker = loc.marker;

        infowindow.addListener("closeclick", function() {
            infowindow.marker = null;
        });

        // Create a new StreetViewService object
        const streetViewService = new google.maps.StreetViewService();
        const radius = 50;

        // Define a callback for streetViewService.getPanoramaByLocation()
        function getStreetView(data, status) {
            if (status === google.maps.StreetViewStatus.OK) {
                const nearStreetViewLocation = data.location.latLng;

                const heading = google.maps.geometry.spherical.computeHeading(
                    nearStreetViewLocation, loc.marker.position);
                infowindow.setContent("<h1>" + loc.title + "</h1>" + 
                                      "<p>" + loc.address + "</p>" +
                                      '<div id="pano"></div>');
                
                const panoramaOptions = {
                    position: nearStreetViewLocation, 
                    pov: {
                        heading: heading,
                        pitch: 30
                    }
                };
                const panorama = new google.maps.StreetViewPanorama(document.getElementById('pano'), panoramaOptions);
            } else {
                infowindow.setContent("<h1>" + loc.title + "</h1>" + 
                                      "<p>" + loc.address + "</p>" +
                                      '<div>No Street View Available</div>');
            }
        }

        streetViewService.getPanoramaByLocation(loc.marker.position, radius, getStreetView);
        infowindow.open(map, loc.marker);
    }
}

function callFourSquareVenuesApi(loc) {
    const url = 'https://api.foursquare.com/v2/venues/search?ll=' + 
                loc.location.lat + ',' + loc.location.lng + '&client_id=' + CLIENT_ID + 
                '&client_secret=' + CLIENT_SECRET + '&v=20160118' + '&query=' + loc.title;

    $.ajax({
        url: url,
    })
    .done(function(data) {
        const venues = data.response.venues;
        if (venues && venues.length > 0) {
            loc.address = venues[0].location.formattedAddress.join("<br/>");
        } else {
            loc.address = "No data returned from FourSquare Venue API";
        }
    })
    .fail(function(status, error) {
        loc.address = "Error calling the FourSquare Venue API."
    });
}