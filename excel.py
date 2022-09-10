
import xlwings
import xlwings as xw 
app = xw.App(visible=True,add_book=False)
# wb = app.books.add()
# wb = app.books.open('example.xlsx')
wb = xw.Book('example.xlsx')
wb.save('example.xlsx')
# app_obj = xlwings.App()

# app_obj.display_alerts=False
# app_obj.screen_updating=False

#app_obj.quit()
