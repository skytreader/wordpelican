# WordPelican

Cross post from Wordpress to Pelican.

## Usage

Invoke the script with the details of the WordPress database.

    python wordpelican.py -h db_host -p db_port -u db_username -P db_password -o output_dir

For each post in your WordPress installation, you get a corresponding file in
the specified output directory.
