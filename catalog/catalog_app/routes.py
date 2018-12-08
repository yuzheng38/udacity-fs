import json
import os
import random
import requests
import string
from catalog_app import app, db
from catalog_app.models import Player, Class, Toon
from datetime import datetime
from flask import abort, flash, jsonify, redirect, render_template, request, session, url_for


STATE = 'XHU4FUHR5X0NQ09TH9CLY6WQH8HCIWG6'  # os.environ['STATE']
CLIENT_ID = '1055575944505-g3be1f62ajs2rtbr16tfdi54td564k4s.\
            apps.googleusercontent.com'  # os.environ['CLIENT_ID']
CLIENT_SECRET = 'Fq9Sfuo0XOWmh-gRYy7rovhe'  # os.environ['CLIENT_SECRET']
SCOPE = 'openid email'
REDIRECT_URI = 'http://localhost:5000/login'
AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'


@app.route('/')
@app.route('/catalog')
def get_catalog():
    """Returns the home page that shows most recently created toons."""
    classes = Class.query.order_by(Class.class_name).all()
    toons = Toon.query.order_by(db.desc(Toon.created))
    if toons.count() == 0:
        flash('There are no toons. Create some new toons!', 'warning')
    return render_template('catalog.html', classes=classes,
                           toons=toons, state=STATE)


@app.route('/catalog/<int:class_id>')
@app.route('/catalog/<int:class_id>/items')
def get_class(class_id):
    """Displays toons belonging to the selected class."""
    classes = Class.query.order_by(Class.class_name).all()
    clazz = Class.query.get_or_404(class_id)
    toons_in_class = Toon.query.filter_by(toon_class_id=class_id)
    if toons_in_class.count() == 0:
        flash('There are no toons in this class. Create some new toons!',
              'warning')
    return render_template('catalog.html', classes=classes,
                           toons=toons_in_class,
                           title=clazz.class_name, state=STATE)


@app.route('/about')
def about():
    """Returns the about page."""
    classes = Class.query.order_by(Class.class_name).all()
    return render_template('about.html', classes=classes,
                           title='About', state=STATE)


@app.route('/account')
def account():
    """Returns the account page."""
    if not session.get('userinfo'):
        flash('You need to log in.', category='danger')
        abort(403)

    classes = Class.query.order_by(Class.class_name).all()
    userinfo = session.get('userinfo')

    return render_template('account.html', classes=classes,
                           title='Account', userinfo=userinfo)


def generate_credentials(auth_code):
    """Retrieves access token from Google with a one-time auth code."""
    token_uri = 'https://www.googleapis.com/oauth2/v3/token'
    data = {
        'code': auth_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }

    res = requests.post(token_uri, data=data)
    return res.json()


def generate_userinfo():
    """Retrieves user info from Google with access token."""
    userinfo_uri = 'https://www.googleapis.com/oauth2/v2/userinfo'
    credentials = session.get('credentials')

    params = {
        'alt': 'json',
        'access_token': credentials['access_token']
    }
    res = requests.get(userinfo_uri, params=params)
    return res.json()


def generate_auth_url():
    """A helper function that generates auth url."""
    url = ('{}?scope={}&client_id={}&redirect_uri={}'
           '&access_type={}&state={}&include_granted_scopes={}'
           '&response_type={}').format(AUTH_URI,
                                       SCOPE,
                                       CLIENT_ID,
                                       REDIRECT_URI,
                                       'offline',
                                       session['state'],
                                       'true',
                                       'code')
    return url


@app.route('/login', methods=['GET', 'POST'])
def login():
    """"""
    if not session.get('state'):
        session['state'] = STATE

    # to guard against CSRF attacks
    if 'state' in request.args and \
            request.args.get('state') != session['state']:
        abort(400)

    # Present user with the Google Sign in prompt to request authorization code
    if 'code' not in request.args:
        auth_url = generate_auth_url()
        return redirect(auth_url)

    # with auth code, request access token
    code = request.args.get('code')
    credentials = generate_credentials(code)

    if credentials.get('error'):    # error requesting access token via Oauth2
        abort(500)
    session['credentials'] = credentials

    # with access token, request user info
    userinfo = generate_userinfo()
    session['userinfo'] = userinfo

    # if user exists, redirect the user to home page
    existing_user = Player.query.get(userinfo['email'])
    if existing_user:
        flash('You have been logged in!', category='success')
        return redirect(url_for('get_catalog'))

    # if user does not exist, create a new user and then redirect to home page
    player = Player(email=userinfo['email'],
                    username=userinfo['name'],
                    picture=userinfo['picture'],
                    password_hash=userinfo['id'])
    db.session.add(player)
    db.session.commit()
    flash('An account was created for you using your profile.',
          category='success')
    return redirect(url_for('get_catalog'))


def revoke_token():
    at = session.get('credentials')['access_token']
    if at:
        url = 'https://accounts.google.com/o/oauth2/revoke?token={}'.format(at)
        _ = requests.get(url)


@app.route('/logout')
def logout():
    """Revokes the token and removes userinfo and credentials from session."""
    revoke_token()  # revoke the access token

    if session.get('userinfo'):
        session.pop('userinfo')
    if session.get('credentials'):
        session.pop('credentials')

    flash('You have been logged out.', 'warning')
    return redirect(url_for('get_catalog'))


@app.route('/catalog/add', methods=['GET', 'POST'])
def add_item_to_catalog():
    """Creates a new item to add to the catalog."""
    if not session.get('userinfo'):
        flash('You need to log in.', category='danger')
        abort(403)

    classes = Class.query.order_by(Class.class_name).all()
    if request.method == 'GET':
        return render_template('new_toon.html', classes=classes,
                               title='New Toon', state=STATE)

    name = request.form['toon_name']
    c = request.form['toon_class']
    desc = request.form['toon_desc']
    toon = Toon(name=name, description=desc, created=datetime.utcnow(),
                toon_class_id=c, toon_player=session.get('userinfo')['email'])
    db.session.add(toon)
    db.session.commit()
    flash('New toon created successfully!', category='success')
    return redirect(url_for('get_catalog'))


@app.route('/catalog/<category>/items/<int:item_id>')
def get_item(category, item_id):
    """Returns the selected item."""
    classes = Class.query.order_by(Class.class_name).all()
    toon = Toon.query.get_or_404(item_id)
    return render_template('item.html', classes=classes,
                           title='Toon', toon=toon, state=STATE)


@app.route('/catalog/<category>/items/<int:item_id>/edit',
           methods=['GET', 'POST'])
def edit_item(category, item_id):
    """Edits the selected item."""

    # if the user is not logged in, abort with 403.
    if not session.get('userinfo'):
        flash('You need to log in first.', category='danger')
        abort(403)

    classes = Class.query.order_by(Class.class_name).all()
    toon = Toon.query.get_or_404(item_id)

    if toon.player.email != session.get('userinfo')['email']:
        abort(403)

    if request.method == 'GET':
        return render_template('new_toon.html', toon=toon,
                               classes=classes, title='Edit')

    if toon.name == request.form.get('toon_name') and \
            toon.toon_class_id == request.form.get('toon_class') and \
            toon.description == request.form.get('toon_desc'):
        return redirect(url_for('get_item', item_id=item_id,
                        category=toon.toon_class_id))

    # field validations are done in HTML
    toon.name = request.form['toon_name']
    toon.toon_class_id = request.form['toon_class']
    toon.description = request.form['toon_desc']
    db.session.add(toon)
    db.session.commit()
    flash('Toon updated successfully!', category='success')
    return redirect(url_for('get_item', item_id=item_id,
                    category=toon.toon_class_id))


@app.route('/catalog/<category>/items/<int:item_id>/delete',
           methods=['POST', 'GET'])
def delete_item(category, item_id):
    """Deletes the selected item from the application database."""

    # if the user is not logged in, abort with 403.
    if not session.get('userinfo'):
        flash('You need to log in first.', category='danger')
        abort(403)

    # if the logged in user is not the same as the item's creator,
    # abort with 403.
    toon = Toon.query.get_or_404(item_id)
    if toon.player.email != session.get('userinfo')['email']:
        abort(403)

    if toon:
        db.session.delete(toon)
        db.session.commit()
        flash('Toon deleted successfully!', category='success')
    return redirect(url_for('get_catalog'))


@app.route('/api/v1/toons')
def get_toons_api():
    """Returns all toons in JSON format."""
    toons = Toon.query.all()
    return jsonify(catalog=[t.serialize for t in toons])


@app.route('/api/v1/toons/<int:toon_id>')
def get_toon_api(toon_id):
    """Returns specified toon in JSON format."""
    toon = Toon.query.get_or_404(toon_id)
    return jsonify(toon=toon.serialize)


@app.route('/api/v1/classes')
def get_classes_api():
    """Returns all playable classes in JSON format."""
    classes = Class.query.all()
    return jsonify(classes=[c.serialize for c in classes])


@app.errorhandler(404)
def error_404(error):
    return render_template('errors/404.html'), 404


@app.errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403


@app.errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500
