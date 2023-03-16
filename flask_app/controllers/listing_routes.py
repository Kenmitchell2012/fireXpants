from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import listing_model, user_model

@app.route('/dashboard')
def user_dash():

    return render_template('view_all.html', all_listings= listing_model.Listing.get_all_listings() )