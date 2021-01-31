from flask import Flask, request, render_template, url_for
import pandas as pd
from pandas import read_csv
from xlsxwriter.workbook import Workbook
from openpyxl import Workbook

app = Flask(__name__)

def convert(file1, file2, file3):
	writer= pd.ExcelWriter('output_file.xlsx', engine='openpyxl')
	op_file1= read_csv("file1.csv", index_col=False)
	op_file2 = read_csv("file2.csv", index_col=False)
	op_file3 = read_csv("file3.csv", index_col=False)
	op_file1.to_excel(writer,'Sheet1')
	op_file2.to_excel(writer, 'Sheet2')
	op_file3.to_excel(writer, 'Sheet3')
	writer.save()




@app.route("/", methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		try:
			file1 = request.files['filename1']
			file1.save("file1.csv")
		except:
			pass
		try:
			file2 = request.files['filename2']
			file2.save("file2.csv")
		except:
			pass
		try:
			file3 = request.files['filename3']
			file3.save("file3.csv")
		except:
			pass

		convert(file1="file1.csv", file2="file2.csv", file3="file3.csv")
	return render_template("index.html")
if __name__=='__main__':
    app.run(debug=True)