$(function() { //ready
	
	drawGeoChart();
	drawLineChart();
		
	function drawGeoChart() {
		<!-- GEO CHART -->
		$.get("csv/chinese_aggregate_countries.csv", function(csvString) {

			var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
			var tableData = new google.visualization.arrayToDataTable(arrayData);

			var options = {
				chart: {
					title: 'Location-wise tweets'
				},
				colorAxis: {colors: ['#00853f', 'black', '#e31b23']},
				backgroundColor: '#0099FF',
				datalessRegionColor: '#CCFF99',
				defaultColor: '#f5f5f5'
			};

			var chart1 = new google.visualization.GeoChart(document.getElementById("geo_map"));
			chart1.draw(tableData, options);
		});
	}
	
	function drawLineChart() {
		<!-- LINE CHART -->
		$.get("csv/chinese_aggregate_years.csv", function(csvString) {

			var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});
			var tableData = new google.visualization.arrayToDataTable(arrayData);

			var options = {
				chart: {
					title: 'Twitter sentiment trends through the years',
					subtitle: 'Positive, Negative, and Neutral: 2006-2015'
				}
			};

			var chart2 = new google.charts.Line(document.getElementById('line_chart'));
			chart2.draw(tableData, options);
		});
	}
	
	function drawBarChart() {
		<!-- BAR GRAPH -->
		// grab the CSV
		$.get("csv/chinese_full_agg.csv", function(csvString) {

			// transform the CSV string into a 2-dimensional array
			var arrayData3 = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});

			var data3 = new google.visualization.arrayToDataTable(arrayData3);

			var options = {
			  chart: {
				title: 'Twitter sentiments by Country',
				subtitle: 'Positive, Negative, and Neutral: 2006-2015',
			  }
			};

			var chart3 = new google.charts.Bar(document.getElementById('bar_chart'));
			chart3.draw(data3, options);
		});
	}
	
	function drawBubbleChart() {
		<!-- BAR CHART -->
		$.get("csv/chinese_full_agg_bubble.csv", function(csvString) {

			// transform the CSV string into a 2-dimensional array
			var arrayData = $.csv.toArrays(csvString, {onParseValue: $.csv.hooks.castToScalar});

			var data = new google.visualization.arrayToDataTable(arrayData);

			var options = {
			  title: 'Tweet bubbles for different countries.',
			  hAxis: {title: 'Negative'},
			  vAxis: {title: 'Positive'},
			  bubble: {textStyle: {fontSize: 11}},
			  colorAxis: {colors: ['yellow', 'orange', '#800080']},
			  datalessRegionColor: '#CCFF99',
			  defaultColor: '#f5f5f5'

			};
			var chart = new google.visualization.BubbleChart(document.getElementById('bubble_chart'));
			chart.draw(data, options);
		});
	}
	
	function readTextFile(file) {
		var textFile = new XMLHttpRequest();
		textFile.open("GET", file, false);
		textFile.onreadystatechange = function () {
			if(textFile.readyState === 4) {
				if(textFile.status === 200 || textFile.status == 0) {
					text = textFile.responseText;
				}
			}
		}
		textFile.send(null);
	}
	
	function drawWordCloud() {
		readTextFile("csv/chinese_full_agg_text.csv")
		//alert(text)
		var data = new google.visualization.DataTable();
		data.addColumn('string', 'Text1');
		data.addRows(1);
		data.setCell(0,0, text);
		var outputDiv = document.getElementById('word_cloud');
		var wc = new WordCloud(outputDiv);
		wc.draw(data, null);
	}
	
	$('#accordion').find('#headingTwo').on('click', function(){
		div_contents = $('#bar_chart').text()
		if(div_contents != '') {
			console.log('not empty');
			return
		}
		else {
			drawBarChart();
		}
	});
	
	$('#accordion').find('#headingThree').on('click', function(){
		div_contents = $('#bubble_chart').text()
		if(div_contents != '') {
			console.log('not empty');
			return
		}
		else {
			drawBubbleChart();
		}
	});
	
	$('.col-md-6').find('#modalBtn').on('click', function(){
		div_contents = $('#word_cloud').text()
		if(div_contents != '') {
			console.log('not empty');
			return
		}
		else {
			drawWordCloud();
		}
	});
});