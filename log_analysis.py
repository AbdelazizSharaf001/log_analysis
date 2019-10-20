#!/usr/bin/env python3
#	Log analysis v1.0.0
try:
	try:
		# Imports	---------------------------
		# Python standard liberary
		import os
		import sys
		from subprocess import call
		
		# Made Manually
		#	gvar	Global variables for this script
		try:
			from gvar import Prints
		except:
			print('{0}\x1b[31m \t[Fatal] their must be a "gvar.py" file provided with tha script in the same directory{0}\tfind if it\'s name, directory or content changed or get it from the package provided\x1b[0m{0}'.format(os.linesep))
			exit()

		# External
		import psycopg2
		from tabulate import tabulate

	except ImportError:
		print(Prints(0))
		try:
			if (int(input('Choose an option: ')) == 1):
				pkgs = ['psycopg2', 'tabulate']
				for x in pkgs:
					call([sys.executable, '-m', 'pip', 'install', '%s' % (x)])
				print(Prints(1))
			else:
				raise Exception
		except (Exception, OSError) as error:
			print(Prints(2))

	else:
		# Global variables	-------------------
		# Development mode
		Dev	= False

		# DATABASE config
		DBNAME	= 'news'

		# Queries list
		#	[
		#		'query',
		# 		'print 1st row',
		#		'tabulate headers'
		#	]
		DBQ	= [
			[	"""
				SELECT count(title), title
						FROM log, articles
						WHERE articles.slug = overlay(log.path
														placing ''
														from 1
														for 9)
						GROUP BY title
						ORDER BY count DESC
						LIMIT 3;
						""",
				"{0}Most popular three articles of all time:\x1b[32m {0}",
				['Views', 'Article']
			],
			[	"""
				SELECT count(title), name
						FROM log, articles, authors
						WHERE articles.slug = overlay(log.path
														placing ''
														from 1
														for 9)
								AND authors.id = articles.author
						GROUP BY authors.name
						ORDER BY count DESC;
						""",
				"{0}Most popular article authors of all time:\x1b[36m {0}",
				['Views', 'Author']
			],
			[
				"""
				SELECT ROUND(x.c::NUMERIC / y.c::NUMERIC * 100, 2) AS av, x.t
						FROM
							(SELECT to_char(time::date, 'Mon DD, YYYY') AS t,
									count(status) AS c
								FROM log
								WHERE status != '200 OK'
								GROUP BY t) as x,
							(SELECT to_char(time::date, 'Mon DD, YYYY') AS t,
									count(status) AS c
								FROM log
								GROUP BY t) as y
						WHERE x.t = y.t
								and (x.c::NUMERIC / y.c::NUMERIC * 100) > 1
						ORDER BY av DESC;
						""",
				"{0}On which days did more than 1% of requests lead to errors:\x1b[31m {0}",
				['%', 'Date']
			]
		]


		# Functions	---------------------------
		# DB cursor
		#	@var	Q_in:integer	Query index
		def DBcursor(Q_in):
			try:
				db = psycopg2.connect(database = DBNAME)
				c = db.cursor()
				c.execute(DBQ[Q_in][0])
				record = c.fetchall()
				c.close()
			except (Exception, psycopg2.Error) as error :
				print("Error while connecting to PostgreSQL",
					":{0}".format(os.linesep) + error if Dev else '')
			finally:
				#closing database connection.
				try:
					if(db):
						db.close()
					return record
				except Exception:
					print(Prints(3))
					exit()

		def main():
			try:
				for x in range(len(DBQ)):
					print(DBQ[x][1].format(os.linesep)
							+ tabulate([[r[0], r[1]] for r in DBcursor(x)],
										headers=DBQ[x][2])
							+ '\x1b[0m')
			except Exception as error:
				print(error if Dev else Prints(4))
				exit()


		# Main script	-----------------------
		if __name__ == '__main__':
				main()

except KeyboardInterrupt:
	print(Prints[5])