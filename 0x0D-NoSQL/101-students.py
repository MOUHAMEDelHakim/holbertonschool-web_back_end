#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """ List all students sorted by score """
    return mongo_collection.aggregate([
        {
            '$project': {
                'name': '$name',
                'averageScore': {'$avg': "$topics.score"}
            }
        },
        {
            '$sort': {"averageScore": -1}
        }
    ])
