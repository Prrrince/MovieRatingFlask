from getpass import getpass
import sys

from movierating import app, bcrypt, db
from movierating.models import User


def main():
    """Main entry point for script."""
    with app.app_context():
        db.metadata.create_all(db.engine)
        if User.query.filter_by(is_admin=True).all():
            create = input('A user already exists! Create another? (y/n):')
            if create == 'n':
                return
        username = input('Enter username: ')
        email = input('Enter email address: ')
        password = getpass('Enter password: ')
        if not password == getpass('Enter password (again): '):
            print('Password didn\'t match')
            return

        user = User(
            username=username,
            email=email,
            password=bcrypt.generate_password_hash(password),
            is_admin=True)
        db.session.add(user)
        db.session.commit()
        print('SuperUser Created Successfully')


if __name__ == '__main__':
    sys.exit(main())
