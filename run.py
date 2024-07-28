from app import create_app
from app.models import db
from flask.cli import FlaskGroup

# Create the app
app = create_app()

# Create a FlaskGroup for CLI commands
cli = FlaskGroup(create_app=create_app)

# Add database commands to the CLI
@cli.command('db_create')
def db_create():
    """Creates the database tables."""
    db.create_all()
    print('Database created!')

@cli.command('db_drop')
def db_drop():
    """Drops the database tables."""
    db.drop_all()
    print('Database dropped!')

# Run the application
if __name__ == '__main__':
    cli()  # Use the FlaskGroup CLI
