// import 'babel-polyfill';

var React = require('react');
var ReactDOM = require('react-dom');


// var LeaveTime = React.createClass({
//     render: function() {
//         console.log(this.props.leaveTime);
//         let data = this.props.leaveTime;

//         if (data.leave_time < 0) {
//             return null;
//         } else {
//             return (
//                 <div className="eta-display">
//                     <div>
//                         <h3>{data.station_name}</h3>
//                     </div>

//                     <div>
//                         <h5>{ data.route_name }</h5>
//                         <span className="leave-time">
//                             Leave in { data.leave_time } mins.
//                         </span>
//                         <span className="eta-and-walk-time">
//                             ({ data.eta } mins - { this.props.walkTime } mins walk time)
//                         </span>
//                     </div>
//                 </div>
//             );
//         }
//     }
// });

class MattDowellContainer extends React.Component {
    // getInitialState() {
    //     return {data: null};
    // }
    constructor () {
        super();
        // this.data = null;
        // this.setState({test: "test"})

        this.getData();
    }

    getData() {
        var self = this;

        fetch('/api')
        .then(function (response) {
            return response.json();
        })
        .then(function (json) {
            self.setState({data: json});
        })
        .catch(function(response) {console.log(response.message)} )
        ;
    }

    renderETA(item, i) {
        // return item.leave_times.map(function(lt) {
        //     // return <LeaveTime leaveTime={lt} walkTime={item.walk_time_min} />;
        //     return <p>test</p>
        // })
        return <p key={i}>inside</p>;
    }

    // componentDidMount() {
    //     console.log("COOMPNTENT MOUNTED");
    //     this.getData(this);
    // }

    render () {
        if (this.state) {
            // console.log(this.state.data.map(a => a));
            // return <div>I did it</div>
            let data = this.state.data;
            console.log(data)
            return (
                <div className="container">
                    test
                    {data ? data.map((obj, i) => this.renderETA(obj, i)) : "no data"}
                    {/*data ? data.map(a => <p>inside</p>) : "no data"*/}
                </div>
            );
        } else {
            return <h1>Loading...</h1>
        }
    }
};

ReactDOM.render(<MattDowellContainer />, document.getElementById('mount-point') );
