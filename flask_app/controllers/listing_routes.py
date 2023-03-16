from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import listing_model, user_model

@app.route('/listings')
def user_dash():
# all_listings= listing_model.Listing.get_all_listings()
    return render_template('view_all.html',  )

@app.route('/listings/new')
def create_form():
    return render_template('create_form.html')

@app.route('/listings/edit')
def edit_form():
    return render_template('edit_form.html')


#view one
@app.route('/listings/one')
def view_one():
    return render_template('view_one.html')

# #create/POST w/ validation
# @app.route('/listings/create', methods=['POST'])
# def create_listing():
#     pass




# #update/POST w/ validation
# @app.route('/listings/update/', methods=['POST'])
# def update_listing():
#     pass

# #delete
# @app.route()
# def delete_listing():
#     pass

# #coolit/deduct 1 from stoke_val
# @app.route()
# def cool_it():
#     pass


# #stokeit/add 1 to stoke_val
# @app.route('listings/stoke_it')
# def stoke_it():
#     pass