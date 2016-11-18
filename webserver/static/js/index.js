// 基于准备好的dom，初始化echarts实例
			var myChart = echarts.init(document.getElementById('main'));

			// 指定图表的配置项和数据
			var option = {
//				title: {
//					text: '自定义雷达图'
//				},
//				legend: {
//					data: ['图一', '图二', '张三', '李四']
//				},
				radar: [

					{
						indicator: [{
							text: '语文',
							max: 150
						}, {
							text: '数学',
							max: 150
						}, {
							text: '英语',
							max: 150
						}, {
							text: '物理',
							max: 120
						}, {
							text: '化学',
							max: 108
						}],
						center: ['50%', '50%'],
						radius: 90,//半径
						
						startAngle: 90,
						splitNumber: 4,
//						shape: 'circle',
						name: {
							formatter: '{value}',
							textStyle: {
								color: '#83d3f9',
								fontSize:15,
								
							},
							
						},
						splitArea: {
							areaStyle: {
								color: ['#83d3f9','#aee5ff', '#c8eeff','#def5ff'],
//								shadowColor: 'rgba(0, 0, 0, 0.3)',
//								shadowBlur: 10
							}
						},
						axisLine: {
							show:false,
							lineStyle: {
								
								color: 'rgba(255, 255, 255, 0.5)'
							}
						},
						splitLine: {
							show:false,
							lineStyle: {
								color: 'rgba(255, 255, 255, 0.3)'
								 
							}
						}
					}
				],
				series: [{
					name: '成绩单',
					type: 'radar',
					data: [{
						value: [120, 118, 130, 100, 99],
						name: '张三',
						symbol:'none',
						label: {
							normal: {
								show: true,
								formatter: function(params) {
									return params.value;
								}
							}
						},
						lineStyle: {
							normal: {
								type:'solid',
								color: '#c0e9fc'
//								color: 'red'
							}
						},
						areaStyle: {
							normal: {
								color: 'rgba(255, 255, 255, 0.5)'
//								color: 'pink',
//								opacity:0.5
							}
						}
					}]
				}]
			}

			// 使用刚指定的配置项和数据显示图表。
			myChart.setOption(option);