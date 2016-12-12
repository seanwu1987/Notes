import pypyodbc
import lucene
import sys
from java.io import File
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser


class IndexSql(object):
	"""Usage: python CreateIndex or python SearchQuery"""
	def GetPoems(self):
		connection = pypyodbc.connect('Driver={SQL Server};Server=***;Database=***;uid=***;pwd=***;')
		cursor = connection.cursor()
		sqlcommand = ("SELECT text FROM table")
		cursor.execute(sqlcommand)
		query = cursor.fetchone()
		cells = []
		while query:
			text = str(query)
			##text.decode('unicode-escape')
			cells.append(text)
			query = cursor.fetchone()
		cursor.close()
		return cells
		
	def CreateIndex(self):
		analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)	
		store = SimpleFSDirectory(File('D:\Code\PythonLearning\Python\idx'))
		config = IndexWriterConfig(Version.LUCENE_CURRENT, analyzer)
		config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
		writer = IndexWriter(store, config)
		
		doc = Document()
		for text in GetPoems():
			field = Field("content", text, Field.Store.YES, Field.Index.ANALYZED)
			doc.add(field)
		writer.addDocument(doc)
		writer.commit()
		writer.close()
		
	def SearchQuery(self):
		analyzer = StandardAnalyzer(Version.LUCENE_CURRENT)	
		store = SimpleFSDirectory(File('D:\Code\PythonLearning\Python\idx'))
		searcher = IndexSearcher(DirectoryReader.open(store))
		query = QueryParser(Version.LUCENE_CURRENT, "content", analyzer).parse(raw_input("Query:"))
		scoreDocs = searcher.search(query, 50).scoreDocs
		for scoreDoc in scoreDocs:
			doc = searcher.doc(scoreDoc.doc)
			print 'content:', doc.get("content")
		del searcher
		
	def __init__(self):
		lucene.initVM()
		print "lucene version is:", lucene.VERSION

		
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print IndexSql.__doc__
		sys.exit(1)
	index = IndexSql()
	try:
		if str(sys.argv[1]) == 'CreateIndex':
			index.CreateIndex()
		elif str(sys.argv[1]) == 'SearchQuery':
			index.SearchQuery()
	except Exception, e:
		print "Failed: ", e
		raise e