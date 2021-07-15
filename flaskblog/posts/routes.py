from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import PostForm 

import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib
import pickle

posts = Blueprint('posts', __name__)


filename = 'nlp_model.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('tranform.pkl','rb')) 
def predict():
 #    df= pd.read_csv("spam.csv", encoding="latin-1")
 #    df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)
    # # Features and Labels
 #    df['label'] = df['class'].map({'ham': 0, 'spam': 1})
 #    X = df['message']
 #    y = df['label']
    
    # # Extract Feature With CountVectorizer
 #    cv = CountVectorizer()
 #    X = cv.fit_transform(X) # Fit the Data
   
 #    pickle.dump(cv, open('tranform.pkl', 'wb'))
   
   
    # from sklearn.model_selection import train_test_split
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
    # #Naive Bayes Classifier
    # from sklearn.naive_bayes import MultinomialNB

    # clf = MultinomialNB()
    # clf.fit(X_train,y_train)
    # clf.score(X_test,y_test)
 #    filename = 'nlp_model.pkl'
 #    pickle.dump(clf, open(filename, 'wb'))
    
    # Alternative Usage of Saved Model
    # joblib.dump(clf, 'NB_spam_model.pkl')
    # NB_spam_model = open('NB_spam_model.pkl','rb')
    # clf = joblib.load(NB_spam_model)

    if request.method == 'POST':
        message = request.form['message']
        data = [message]
        vect = cv.transform(data).toarray()
        my_prediction = clf.predict(vect)
    if my_prediction==1:
        return render_template('1.html')
    else:
        return render_template('0.html')





@posts.route("/post/new", methods=['GET', 'POST']) #posts.routes bz of post blueprint
@login_required
def new_post(cv=cv,clf=clf):
    form = PostForm()
    message=str(form.content.data)
    data2 = [message]
    vect = cv.transform(data2).toarray()
    my_prediction = clf.predict(vect)
    if form.validate_on_submit():
        if my_prediction==1:
            flash('You are posting a spam. Post not created', 'danger')
            return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')
        else:
            post = Post(title=form.title.data, content=form.content.data, author=current_user)
            db.session.add(post)
            db.session.commit()
            flash('Your post has been created!', 'success')
            return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post',
                           form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post',
                           form=form, legend='Update Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))
