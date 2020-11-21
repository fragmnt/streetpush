import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/App.css';

// Mapbox
import mapboxgl from 'mapbox-gl';
mapboxgl.accessToken = 'pk.eyJ1Ijoic2FuenNhbnoiLCJhIjoiY2tocnF2dHFlMDVxczJxbXRqaG16Z2RxNyJ9.m62F8Nt5N-6l1yRCkmNLtQ';

class App extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            lng: -73.95,
              lat: 40.8,
              zoom: 13.5,
              pitch: 45,
              bearing: -25,
              toggled: false,
            // get lng and lat from user permissions. keep zoom level
        }

        this.mapInit = this.mapInit.bind(this);
        this.zoomIn = this.zoomIn.bind(this);
        this.zoomOut = this.zoomOut.bind(this);
        this.toggleChatModal = this.toggleChatModal.bind(this);
    }

    mapInit = () => {
        const map = new mapboxgl.Map({
            container: this.mapContainer,
            style: 'mapbox://styles/mapbox/streets-v11',
            center: [this.state.lng, this.state.lat],
            zoom: this.state.zoom,
            pitch: this.state.pitch, // pitch in degrees
            bearing: this.state.bearing,
        });
        return map;
    }

    componentDidMount = () => {
        var map = this.mapInit();
        map.on('move', () => {
            this.setState({
            lng: map.getCenter().lng.toFixed(4),
            lat: map.getCenter().lat.toFixed(4),
            zoom: map.getZoom().toFixed(2)
            });
        });
    }

    toggleChatModal = () => {
        this.setState({
            toggled: !this.state.toggled,
        });
        console.log(this.state.toggled)
    }

    zoomIn = (e) => {
        e.preventDefault();
        var map = this.mapInit();
        //var zX = map.getZoom();
        // var diff = 0.5;
        map.zoomIn({duration: 1000});
    }

    zoomOut = (e) => {
        e.preventDefault();
        var map = this.mapInit();
       // var zY = map.getZoom();
       // var diff = 0.5;
        map.zoomOut({duration: 1000});
    }

    render () {
        return (
            <>
                <div>
                    <div className="sidebarStyle">
                        <h3>Streetpush</h3>
                        <div>Longitude: {this.state.lng} | Latitude: {this.state.lat} | Zoom: {this.state.zoom}</div>
                        <input placeholder="Search a place"/>
                    </div>
                    <div>
                        {this.state.toggled ? <div className="sidebarModal">
                            <h3>Civilian Chat</h3>
                            <form>
                                <input placeholder="Send a message"/>
                                <button>Send</button>
                            </form>
                        </div> : null}
                    </div>
                    <div className="menubarStyle">
                        <div className="bubble">
                            <button onClick={this.toggleChatModal}>
                                <img src="public/icons/chat.svg"/>
                            </button>
                            <span>Chat</span>
                        </div>
                        <div className="bubble">
                        <img src="public/icons/alert.svg"/>
                            <span>Alerts/Incidents</span>
                        </div>
                        <div className="bubble">
                        <img src="public/icons/spy.svg"/>
                            <span>Real-time Updates</span>
                        </div>
                        <div className="zoomInOut bubble">
                            <span>Zoom In and Out</span>
                            <button onClick={e => this.zoomIn(e)} className="opt1">+</button>
                            <button onClick={e => this.zoomOut(e)} className="opt2">-</button>
                        </div>
                    </div>
                    <div ref={el => this.mapContainer = el} className="mapContainer"/>
                </div>
            </>
        )
    }
}

export default App;