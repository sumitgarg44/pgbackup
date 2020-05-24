import pytest
from pgbackup import cli
#  $ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups

url = "postgres://bob@example.com:5432/db_one"

def test_parser_without_driver():
	"""
	Without a specified driver the parser will exit
	"""
	with pytest.raises(SystemExit):
		parser = cli.create_parser()
		parser.parse_args([url])

def test_parser_with_driver():
	"""
	The parser will exit  if it receives a driver without a destination
	"""
	with pytest.raises(SystemExit):
		parser = cli.create_parser()
		parser.parse_args([url, "--driver", "local"])

def test_parser_with_driver_and_detination():
	"""
	The parser will not exit if it receives a driver and destination
	"""
	with pytest.raises(SystemExit):
		parser = cli.create_parser()
		parser.parse_args([url, "--driver", "local", "/some/path"])

		assert args.driver == "local"
		assert args.destination == "/some/path"
