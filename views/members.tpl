<!DOCTYPE html>
<html>
<head>
	<title>Notendur</title>
	<link rel="stylesheet" type="text/css" href="../static/style.css">
</head>
<body>
	<h3>Notendur</h3>
	<table>
	% for i in rows:
		<tr>
			<td>{{i[0]}}</td>
			<td>{{i[1]}}</td>
			<td>{{i[2]}}</td>
		</tr>
	% end
	
	</table>
</body>
</html>