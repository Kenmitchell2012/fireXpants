from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import listing_model, user_model

@app.route('/dashboard')
def user_dash():
# all_listings= listing_model.Listing.get_all_listings()
    return render_template('view_all.html',  )

@app.route('/listings/new')
def create_form():
    return render_template('create_form.html')

@app.route('/listings/edit')
def edit_form():
    return render_template('edit_form.html')

