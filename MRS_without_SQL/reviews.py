from utils import *

path = r'MRS_without_SQL\data\reviews.csv'

def get_user_review(user_id):
    reviews = read_csv(path)
    user_review_li = []
    for r in reviews:
        if r['user_id'] == user_id:
            user_review_li.append(r) 
    
    return user_review_li

# print(get_user_review('2'))



def add_review(u_id, m_id, m_rating, m_comment):
    reviews = read_csv(path)

    new_review = {
        'id': generate_id(path),
        'user_id': u_id,
        'movie_id': m_id,
        'rating': m_rating,
        'comment': m_comment
    }

    write_row(path, new_review)