import React from 'react';
import ReactDOM from 'react-dom';
import {BoostrapTable, TableHeaderColumn} from 'react-bootstrap-table';
import DatePicker from 'react-bootstrap-date-picker';


var Login = React.createClass({
    
    preventDefault: function(e){
        e.preventDefault();
    },

    loginUser: function(e){
        var username = this.refs.usernameInput.value;
        var password = this.refs.passwordInput.value;

        this.props.login(username, password);
    },

    registerUser: function(e){
        var username = this.refs.usernameInput.value;
        var password = this.refs.passwordInput.value;

        this.props.register(username, password);
    },

    render: function() {
        return (
            <div className="container">
                <div className="col-md-offset-3 col-md-6">
                    <div className="well">
                        <h3>Log in or Sign Up</h3>
                        <hr/>
                        <form className="form-horizontal" onSubmit={this.preventDefault}>
                            <div className="form-group">
                                <label htmlFor="usernameInput" className="col-sm-2 control-label">Username</label>
                                <div className="col-sm-10">
                                    <input type="text" className="form-control" id="usernameInput"
                                        ref="usernameInput"  placeholder="Username" autoFocus={true} />
                                </div>
                            </div>
                            <div className="form-group">
                                <label htmlFor="passwordInput" className="col-sm-2 control-label">Password</label>
                                <div className="col-sm-10">
                                    <input type="password" className="form-control" id="passwordInput"
                                        ref="passwordInput"  placeholder="Password" />
                                </div>
                            </div>
                            <div className="form-group">
                                <div className="col-sm-offset-2 col-sm-10">
                                    <button onClick={this.loginUser} className="btn btn-default">Log in</button>
                                    <button onClick={this.registerUser} className="btn btn-default">Sign up</button>
                                </div>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
        );
    }
});


var Navbar = React.createClass({
    handleClickLogout: function() {
        this.props.logout();
    },

    render: function() {

        return (
            <nav className="navbar navbar-default">
                <div className="container-fluid">
                    <div className="navbar-header">
                        <span className="navbar-brand">Traveler Planner</span>
                    </div>
                    <div id="navbar" className="navbar-collapse collapse">
                        
                        <ul className="nav navbar-nav navbar-right">
                            <li><p className="navbar-text">Hello, {this.props.username}</p></li>
                                                        
                            <li><a onClick={this.handleClickLogout}>Logout</a></li>
                        </ul>
                    </div>
                </div>
            </nav>
        );
    }
});


var TripsForm = React.createClass({

    getInitialState: function(){
        return {'startDate':'', 'endDate':'', 'destination':'', 'comment':''};
    },

    handleStartDateChange: function(e){
        console.log("newDate", e);
        return this.setState({startDate: e});
    },

    handleEndDateChange: function(e){
        console.log("newDate", e);
        return this.setState({endDate: e});
    },

    handleCommentChange: function(e){
        this.setState({comment: e.target.value});
    },

    handleDestinationChange: function(e){
        this.setState({destination: e.target.value});
    },

    transformDate: function(date){
        var splits = date.split('-');
        return splits[1] + '/' + splits[2] + '/' + splits[0];
    },

    handleSubmit: function(e){
        e.preventDefault();
        var startDate = this.transformDate(this.state.startDate.split('T')[0]);
        var endDate = this.transformDate(this.state.endDate.split('T')[0]);
        var destination = this.state.destination;
        var comment = this.state.comment;

        if(!startDate || !endDate || !destination) return;

        this.props.onTripSubmit({startDate: startDate, endDate: endDate, destination: destination, comment: comment});
        this.setState({startDate: '', endDate: '', destination: '', comment: ''});
    },

    render: function(){
        const margin = {
            marginBottom: '5px'
        };

        return(
            <div className="well">
                <form className="form-horizontal" onSubmit={this.handleSubmit}>
                    <fieldset>
                        <legend>Add new trip</legend>
                        <div className="form-group">
                            <div className="col-md-12 col-lg-12">
                                <input
                                    className="form-control"
                                    type="text"
                                    placeholder="Destination"
                                    value={this.state.destination}
                                    onChange={this.handleDestinationChange}
                                />
                            </div>
                        </div>

                        <div className="form-group">
                            <label htmlFor="inputStartDate" className="col-md-3 control-label">Start Date</label>
                            <div className="col-md-9">
                                <DatePicker id="inputStartDate" 
                                            className="form-control" 
                                            value={this.state.startDate} 
                                            onChange={this.handleStartDateChange}
                                            dateFormat="MM/DD/YYYY" />
                            </div>
                        </div>

                         <div className="form-group">
                            <label htmlFor="inputEndDate" className="col-md-3 control-label">End Date</label>
                            <div className="col-md-9">
                                <DatePicker id="inputEndDate" 
                                            className="form-control" 
                                            value={this.state.endDate} 
                                            onChange={this.handleEndDateChange}
                                            dateFormat="MM/DD/YYYY" />
                            </div>
                        </div>

                        <textarea className="form-control" value={this.state.comment} style={margin} rows="4" placeholder="Comment" onChange={this.handleCommentChange}></textarea>
                        
                        <div className="form-group">
                            <div className="col-md-offset-5 col-lg-offset-5">
                                <button type="submit" className="btn btn-primary">Add trip</button>
                            </div>
                        </div>
                    </fieldset>
                </form>
            </div>
        );
    }
});

var TripsTable = React.createClass({

    onBeforeSaveCell: function(row, cellName, cellValue){
        console.debug(row);
        if(cellName == 'startDate' ){
            return !(new Date(cellValue) == "Invalid Date") 
        }
        if(cellName == 'endDate' ){
            return !(new Date(cellValue) == "Invalid Date") 
        }
    },

    onAferSaveCell: function(row, cellName, cellValue){
        this.props.editTrip(row);
    },

    onAfterDeleteRow: function(tripIDs){
        for(var i=0; i < tripIDs.length; ++i){
            this.props.deleteTrip(tripIDs[i]);
        }
    },


    render: function(){
        var options = {
            afterDeleteRow: this.onAfterDeleteRow
        };

        var cellEditOptions = {
            mode: 'dbclick',
            blurToSave: true,
            beforeSaveCell: this.onBeforeSaveCell,
            afterSaveCell: this.onAferSaveCell
        };

        var selectRowOptions = {
            mode: 'checkbox'
        };

        return(
            <BootstrapTable data={this.props.data} 
                options={options}
                cellEdit={cellEditOptions}
                deleteRow={true}
                selectRow={selectRowOptions}
                pagination={true}
                hover>
                <TableHeaderColumn dataField="tripId" isKey hidden>#Trip</TableHeaderColumn>
                <TableHeaderColumn width="150" dataField="destination">Destination</TableHeaderColumn>
                <TableHeaderColumn dataField="startDate">Start Date</TableHeaderColumn>
                <TableHeaderColumn dataField="endDate">End Date</TableHeaderColumn>
                <TableHeaderColumn dataField="comment">Comment</TableHeaderColumn>
                <TableHeaderColumn dataField="daysToTrip" editable={false}>Days To Trip</TableHeaderColumn>
            </BootstrapTable>
        );
    }
});

var TravelPlanner = React.createClass({
    getInitialState: function(){
		return{
			username: null,
			token: null,
            trips: [],
            fromDate: null,
            toDate: null
		}
    },

    logout: function(){
        this.setState({username: null, token: null});
    },

    login: function(username, password){
        console.debug(username)
        this.ajaxCall({
            method: 'POST',
            url: 'api/token',
            data: JSON.stringify({"username": username, "password": password}),
            success: function(data){
                console.debug('Data ', data);
                this.setState({
                    username: username,
                    token: data['access_token']
                });
            }.bind(this)
        });
    },

    register: function(username, password){
         this.ajaxCall({
            method: 'POST',
            url: 'api/users',
            data: JSON.stringify({"username": username, "password": password}),
            success: function(data){
                console.debug('Data ', data);
                this.login(username, password);
            }.bind(this)
        });
    },

    componentDidUpdate: function(prevProps, prevState){
        if(this.state.token != null && prevState.token == null){
            this.getTrips();
            $("#loginWarning").hide();
        }
    },

    getTrips: function(){
        this.ajaxCall({
            method: 'GET',
            url: 'api/users/' + this.state.username + '/trips',
            success: function(data){
                this.setState({trips: data["trips"]});
            }.bind(this)
        })
    },

    submitTrip: function(data){
        this.ajaxCall({
            method: 'POST',
            url: '/api/users/' + this.state.username + '/trips',
            data: JSON.stringify(data),
            success: function(data){
                this.getTrips();
            }.bind(this)
        })    
    },

    editTrip: function(data){
        console.debug(data);
        this.ajaxCall({
            method: 'PUT',
            url: '/api/users/' + this.state.username + '/trips/' + data["tripId"],
            data: JSON.stringify(data),
            success: function(data){
                this.getTrips();
            }.bind(this)
        })
    },

    deleteTrip: function(id){
        this.ajaxCall({
            method: 'DELETE',
            url: '/api/users/' + this.state.username + '/trips/' + id,
            success: function(data){
                this.getTrips();
            }.bind(this)
        })
    },

    getTripsInNextMonth: function(e){
        e.preventDefault();

        this.ajaxCall({
            method: 'GET',
            url: '/travel-plan',
            success: function(data){
                window.location = '/travel-plan';
            }.bind(this)
        })
    },

    handleFromDateChange: function(e){
        console.log("newDate", e);
        if(e == null && this.state.toDate == null){
            this.getTrips();
        }
        return this.setState({fromDate: e});
    },

    handleToDateChange: function(e){
        console.log("newDate", e);
        if(e == null && this.state.fromDate == null){
            this.getTrips();
        }
        return this.setState({toDate: e});
    },

    filter: function(e){
        e.preventDefault();

        if(!this.state.fromDate || !this.state.toDate) return;

        var startDate = this.state.fromDate.split('T')[0];
        var endDate = this.state.toDate.split('T')[0];

        this.ajaxCall({
            method: 'GET',
            url: '/api/users/' + this.state.username + '/trips/' + startDate + '&' + endDate,
            success: function(data){
                this.setState({trips: data["trips"]});
            }.bind(this)
        })
    },

    ajaxCall: function(settings){
        settings.dataType = 'json';
        settings.contentType = 'application/json';

        settings.error = function(xhr, status, err){
            console.error(settings.url, status, err.toString());
            if(xhr.status == 401){
                $("#loginWarning").html("Username or password wrong. If you are signing up username is taken!");
                $("#loginWarning").show();
                this.logout();
            }
        }.bind(this)

        if(this.state.token != null){
            console.debug(this.state.token);
            settings.beforeSend = function(xhr){
                xhr.setRequestHeader("Authorization", "JWT " + this.state.token);
            }.bind(this)
        }
        console.debug(settings)
        $.ajax(settings);
    },

	render: function(){
		if(this.state.token == null){
			return(
				<div>
					<Login login={this.login} register={this.register}/>
                    <div className="col-md-offset-3 col-md-6">
                        <div className="alert alert-danger" id="loginWarning" hidden></div>
                    </div>
				</div>
			)
		}
        else{
            return(
                <div>
                    <Navbar username={this.state.username} logout={this.logout}/>
                    <div className="container-fluid">
                        <div className="row">
                            <div className="col-md-offset-1 col-md-8">
                                <div className="row">
                                    <div className="col-md-3">
                                        <h2> My Trips </h2>
                                    </div>
                                    <div className="col-md-6">
                                        <form className="form-inline" onSubmit={this.filter}>
                                            <div className="form-group">
                                                <label htmlFor="fromDate">From</label>
                                                <DatePicker id="fromDate" 
                                                            className="form-control" 
                                                            value={this.state.fromDate} 
                                                            onChange={this.handleFromDateChange}
                                                            dateFormat="MM/DD/YYYY" />
                                            </div>
                                            <div className="form-group">
                                                <label htmlFor="toDate">To</label>
                                                <DatePicker id="toDate" 
                                                            className="form-control" 
                                                            value={this.state.toDate} 
                                                            onChange={this.handleToDateChange}
                                                            dateFormat="MM/DD/YYYY" />
                                            </div>
                                            <button type="submit" className="btn btn-default">Filter</button>
                                        </form>
                                    </div>
                                    <div className="col-md-3">
                                        <button style={{float: 'right'}} onClick={this.getTripsInNextMonth} className="btn btn-info">Get next month travel plan</button>
                                    </div>
                                </div>
                                <hr/>
                                <TripsTable data={this.state.trips} editTrip={this.editTrip} deleteTrip={this.deleteTrip}/>
                            </div>
                            <div className="col-md-3">
                                <TripsForm onTripSubmit={this.submitTrip}/>
                            </div>
                        </div>
                    </div>
                </div>
            )
        }
	}
});

ReactDOM.render(
  <TravelPlanner />,
  document.getElementById('app')
);
