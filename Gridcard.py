from flet import *
from Data import grid_list_image

gridcom = GridView(
	expand=3,
	runs_count=5,
	max_extent=150,
	child_aspect_ratio=1,
	spacing=15,
	run_spacing=15

	)

for x in grid_list_image:
	gridcom.controls.append(
		Card(
			elevation=20,
			content=Image(
				src=x,
			fit=ImageFit.COVER,
			border_radius=border_radius.all(10)

				)
			)

		)

gridscreen = Container(
	margin = margin.only(left=20),
	content= Column([
	Text("Ação",weight="bold",size=30,color="white"),
	gridcom

		],scroll="auto")

	)

gridscreen2 = Container(
	margin = margin.only(left=20),
	content= Column([
	Text("Besteirol",weight="bold",size=30,color="white"),
	gridcom

		],scroll="auto")

	)

