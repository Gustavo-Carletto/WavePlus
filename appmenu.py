from flet import *

appmenu = Row([
	CircleAvatar(
		foreground_image_url="https://cdn.dribbble.com/users/60166/screenshots/17459154/media/8c38e117315b2b6c251aa0201f863e70.jpg?resize=400x300&vertical=center"
	),
	Container(
		margin = margin.symmetric(vertical=40),
		content=Row([
			Icon(name="pin_drop",color="white"),
			Text("Brasil",color="white"),
			Icon(name="search",color="white"),

			])
		)


	],alignment="spaceAround")