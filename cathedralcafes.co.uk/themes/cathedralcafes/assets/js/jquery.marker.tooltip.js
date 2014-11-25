/*
 * Bespoke tool-tips for CC
 */

function CustomMarkerToolTip(map, text) {

	this.tooltip = $('<div style="display: none; \
								position: absolute; \
								z-index:20000" \
								class="map-tooltip">' + text + '</div>');
	this.map = map;

	this.get_overlay = function(map) {

		/*
		 * creates and returns an overlay layer that
		* we can use to help get an individual markers
		* coordinates
		*/

		var overlay = new google.maps.OverlayView();
		overlay.draw = function(){}
		overlay.setMap(map);
		return overlay

	};

	//	only calculate this one time per request
	this.overlay = this.get_overlay(this.map);

	this.build_tooltip = function(marker)	{
		var self = this;

		$('#map_canvas').prepend(this.tooltip)
				
		//  Map world relative to map container
		var proj = this.overlay.getProjection();
		var pos = marker.getPosition();
		var p = proj.fromLatLngToContainerPixel(pos);

		var x = p.x - 70 + this.tooltip.width();
		var y = p.y - 30 + this.tooltip.height() / 2;

		//	tune CSS
		this.tooltip.css({ 
			top: y,
			left: x
		});

	};

	this.addMarker = function(marker) {

		var self = this;

		google.maps.event.addListener(marker, 'mouseover', function(event) {
			self.build_tooltip(marker)
			self.tooltip.animate({"opacity": "toggle"}, 300);
		});

		google.maps.event.addListener(marker, 'mouseout', function(event) {
			self.tooltip.fadeOut(0);
		});

	}

};