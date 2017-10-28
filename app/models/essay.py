import random
from faker import Faker
from .. import db


class Essay(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, index=True)
    student_profile_id = db.Column(
        db.Integer,
        db.ForeignKey('student_profile.id'),
        nullable=False,
        index=True
    )
    link = db.Column(db.String, index=True)

    @staticmethod
    def generate_fake(count=2):
        fake = Faker()
        essay_names = random.sample([
            'UPenn Why Essay',
            'Dartmouth Supplemental Essay',
            'Columbia Why Essay',
            'Cornell Engineering Essay',
            'NYU Business Why Essay',
            'M&T Supplemental',
            'Vagelos Supplemental',
            'MIT Activity Essay',
            'UChicago Community Supplemental',
            'Harvard Why Essay'
        ], count)
        essays = []
        for i in range(count):
            essays.append(Essay(
                name=essay_names[i],
                link="https://google.com"
            ))
        return essays

    def __repr__(self):
        return '<Essay {}, {}>'.format(self.name, self.link)