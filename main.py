from nicegui import ui

ui.label("add delete edit button")

# NOW CREATE COLUMN AND ROWS TABLE
columns = [
	{"name":"name","label":"Name","field":"name"},
	{"name":"age","label":"Age","field":"age"},
	{"name":"actions","label":"Actions","field":"actions"},
]

rows =[
	{"id":0,"name":"joko","age":43,"actions":["edit","delete"]},
	{"id":1,"name":"dadang","age":65,"actions":["edit","delete"]},
	{"id":2,"name":"kio","actions":["edit","delete"]},
	{"id":3,"name":"lop","actions":["edit","delete"]},

]


# NOW DELETE DATA IN TABLE
def deletenow(deldata):
	print("you will delete")
	# NOW FIND DATA FOR DELETE IN ALL DATA IN table.rows
	for i,x in enumerate(table.rows):
		if x['id'] == deldata['args']['id']:
			# IF FOUND THEN DELETE NOW
			del table.rows[i]
			# NOW UPDATE AGAIN TABLE
			# THIS FOR REFRESH TABLE
			table.update()
			break
	# NOW CLOSE DIALOG
	dialog.close()

	# NOW SEE RESULT
	print(table.rows)




# NOW CREATE DIALOG FOR DETAIL YOU CLICK 
# IF YOU CLICK EDIT BUTTON IN TABLE THEN SHOW DIALOG
# FOR SHOW NAME AND AGE DETAILS
def opendialog(msg,youaction):
	with ui.dialog() as dialog,ui.card():
		ui.label(youaction).classes("text-h3")
		# AND NOW SHOW LABEL NAME 
		# FOR DETAILS ABOUT args CHECK WITH PRINT(msg)
		ui.label(f"name : {msg['args']['name']}").classes("text-h4")

		# AND for AGE I SET NO DATA IF NO daTA THEN SHOW TEXT NO DATA
		age = msg['args'].get("age")

		# NOW IF AGE IS NONE THEN SHOW NONE
		if age is not None:
			ui.label(f"age : {age}").classes("text-h4")
		else:
			ui.label(f"NO AGE DATA AVAILABLE").classes("text-h4")
		
		# AND NOW FOR DELETE BUTTON IF youaction is delete
		if youaction == "delete":
			ui.button("delete now",on_click=lambda e:deletenow(msg)).classes("bg-red")
	# I FORGOT FOR OPEN DIALOG
	dialog.open()









# AND NOW CREATE VALUE OF YOU CLICK IN BUTTON EDiT LIKE NAME AND AGE
def you_run_edit(msg):
	print(msg)
	opendialog(msg,"edit")

def you_run_delete(msg):
	print(msg)
	opendialog(msg,"delete")



# AND NOW ADD ROWS AND COLUMN TO TABLE
with ui.table(columns=columns,rows=rows,row_key="name") as table:
	# AND NOW MODIFY THE TABLE WITH ADD_SLOT 
	table.add_slot("header",r'''
		<q-tr :props="props">
			<q-th v-for="c in props.cols">
			{{c.label}}
			</q-th>
		</q-tr>

		''')
	# NOW FOR BODY YOU TABLE HERE
	table.add_slot("body",r'''
        <q-tr :props="props">
            <q-td v-for="c in props.cols">
            <q-btn :color="a == 'delete' ? 'red':'blue'" v-if="c.name == 'actions'" 
            v-for="a in c.value"
            :key="a"
            @click="a == 'edit' ? $parent.$emit('you_run_edit',props.row) : $parent.$emit('you_run_delete',props.row)"
            :label="a"

            />

            <span v-else>
                {{c.value}}
            </span>
            </q-td>
        </q-tr>
        ''')
	# NOW ADD LISTENER IF YOU CLICK EDIT BUTToN IN TABLE
	table.on("you_run_edit",lambda msg:you_run_edit(msg))

	# AND NOW ADD IF YOU CLICK DELETE BUTTON IN TABLE 
	# THEN RUN FUNCTION
	table.on("you_run_delete",lambda msg:you_run_delete(msg))


# NOW RUN IN DESKTOP MODE
ui.run(native=True)
