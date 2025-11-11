import sqlite3

def dict_factory(cursor, row):
 fields = []
 # Extract column names from cursor description
 for column in cursor.description:
    fields.append(column[0])

 # Create a dictionary where keys are column names and values are row values
 result_dict = {}
 for i in range(len(fields)):
    result_dict[fields[i]] = row[i]

 return result_dict

class DB:
	def __init__(self, dbfilename):
		self.dbfilename = dbfilename
		self.connection = sqlite3.connect(self.dbfilename)
		self.cursor = self.connection.cursor()
	
	def readAllRecords(self):
		self.cursor.execute("SELECT * FROM trails")
		rows = self.cursor.fetchall()
		all = []
		for row in rows:
			d = dict_factory(self.cursor, row)
			all.append(d)
		print("the rows are", rows)
		return all

	def saveRecord(self, record):
		data = [record['name'], record['movie'], record['genre'], record['rating'], record['review']]
		#self.cursor.execute("INSERT INTO trails (name, description, length, rating) VALUES (?, ?, ?, ?)", record)
		self.cursor.execute("INSERT INTO trails (name, movie, genre, rating, review) VALUES (?, ?, ?, ?, ?)", data)
		self.connection.commit()

	def editRecord(self, id, d):
		data = [d['name'], d['movie'], d['genre'], d['rating'], d['review'], id]
		self.cursor.execute("UPDATE trails SET name=?, movie=?, genre=?, rating=?, review=? WHERE id=?", data)
		self.connection.commit()

	def deleterecord(self, id):
		self.cursor.execute("DELETE FROM trails WHERE id=?", [id])
		self.connection.commit()

	def getReview(self, id):
		self.cursor.execute("SELECT * FROM trails WHERE id=?", [id])
		row = self.cursor.fetchone()
		if row:
			return dict_factory(self.cursor, row)
		return None

	def close(self):
		self.connection.close()

if __name__ == "__main__":
	db = DB("trails.db")
	db.readAllRecords()
	db.saveRecord(1)
	db.readAllRecords()
	db.close()