import pytest

import subprocess

from pgbackup import pgdump

url = "postgres://bob:password@example.com:4532/db_one"

def test_dump_calls_pg_dump(mocker):
	"""
	Utilize pgdump with database URL
	"""
	mocker.patch('subprocess.Popen')
	assert pgdump.dump(url)
	subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

def test_dump_handles_os_error(mocker):
	"""
	pgdump.dump returns a reasonable error if pg_dump isn't installed
	"""
	mocker.patch('subprocess.Popen', side_effect=OSError('no such file'))
	with pytest.raises(SystemExit):
		pgdump.dump(url)

def test_dump_file_without_timestamp():
	"""
	pgdump.dump_file_name retunrs the name of the database 
	"""
	assert pgdump.dump_file_name(url) == 'db_one.sql'

def test_dump_file_with_timestamp():
	"""
	pgdump.dump_file_name retunrs the name of the database with timestmap
	"""

	timestamp = "2019-12-28T13:14:14"
	assert pgdump.dump_file_name(url, timestamp) == f"db_one-{timestamp}.sql"
