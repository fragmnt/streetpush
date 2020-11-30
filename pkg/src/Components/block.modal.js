import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/BlockModal.css';
import bent from 'bent';

let BASE_API_URL = 'http://localhost:8000'
let SIGNUP_PATH = '/auth/users/'
let LOGIN_PATH = '/auth/token/login/'


class BlockModal extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            closed: !false,
            isAuthenticated: false,
            tabSwitch: 0,
            lusername: '',
            lpassword: '',
            susername: '',
            spassword: '',
            semail: '',
        }
        this.onChange = this.onChange.bind(this);
        this.toggleSignInModule = this.toggleSignInModule.bind(this);
        this.loginToAPI = this.loginToAPI.bind(this);
        this.signUpToAPI = this.signUpToAPI.bind(this);
        this.loginAfterSignup = this.loginAfterSignup.bind(this);
        this.tabSwitch = this.tabSwitch.bind(this);
    }

    onChange = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    }

    loginToAPI = async (e) => {
        const { lusername, lpassword } = this.state;
        e.preventDefault();
        var formData = {
            username: lusername, 
            password: lpassword
        };
        const post = bent(BASE_API_URL, 'POST', 'json', 200);
        const response = await post(LOGIN_PATH, formData);
       
        sessionStorage.setItem('authToken', response.auth_token)
        sessionStorage.setItem('username', lusername)
        this.setState({ isAuthenticated: true});
        this.setState({
            closed: !this.state.closed,
        });

        // push to map or chats
    }

    signUpToAPI = async (e) => {
        const { semail, spassword, susername } = this.state;
        e.preventDefault();

        var formData = {
            username: susername, 
            email: semail,
            password: spassword
        };

        const post = bent(BASE_API_URL, 'POST', 'json', 201, 400);
        const response = await post(SIGNUP_PATH, formData);
        console.log(response);

        alert("Your account has been created. You will be signed in automatically")
        this.loginAfterSignup(formData.username, formData.password);
    }

    loginAfterSignup = async(u, p) => {

        var formData = {
            username: u, 
            password: p,
        };

        const post = bent(BASE_API_URL, 'POST', 'json', 200);
        const response = await post(LOGIN_PATH, formData);
       
        sessionStorage.setItem('authToken', response.auth_token)
        sessionStorage.setItem('username', u)
        this.setState({ isAuthenticated: true});
        this.setState({
            closed: !this.state.closed,
        });
    }

    toggleSignInModule = () => {
        if (this.state.isAuthenticated == false) {
            alert('You must sign in or signup first!')
        } else {
            this.setState({
                closed: !this.state.closed,
            });
        };
    }

    tabSwitch = (number) => {
        if (number == 0) {
            this.setState({
                tabSwitch: 0,
            }); 
        }
        else {
            this.setState({
                tabSwitch: 1,
            }); 
        }
    }

    render () {

        const { lusername, lpassword } = this.state;
        const { semail, spassword, susername } = this.state;

        return (
            <>
            {this.state.closed ?  <div className="modal_bg">
                <div className="modal">
                    
                <div className="tabs">
                    <div className="tab">
                        <button
                        onClick={() => this.tabSwitch(0)}
                        >Login</button>
                    </div>
                    <div className="tab">
                    <button
                        onClick={() => this.tabSwitch(1)}
                        >Signup</button>
                    </div>
                </div>
                    {this.state.tabSwitch == 0 ? <>
                        <button onClick={() => this.toggleSignInModule()}
                    className="closeBtn">close</button>
                    <div className="txt_wrapper">
                        <h3>Login</h3>
                        <form>
                            <label>Username</label><br/>
                            <input type="text"
                                name="lusername"
                                value={lusername} ref={this.input}
                                onChange={this.onChange}/>
                            <br/>

                            <label>Password</label><br/>
                            <input type="password"
                                name="lpassword"
                                value={lpassword}
                                onChange={this.onChange}/>
                        </form>
                        <button 
                        type="submit"
                        className="btn"
                        onClick={this.loginToAPI}>Log in
                        </button>
                    </div></> : 
                    <>
                     <button onClick={() => this.toggleSignInModule()}
                        className="closeBtn">close</button>
                         <div className="txt_wrapper">
                        <h3>Signup</h3>
                        <form>
                            <label>Email</label><br/>
                            <input type="text"
                                name="semail"
                                value={semail} ref={this.input}
                                onChange={this.onChange}/>
                            <br/>

                            <label>Username</label><br/>
                            <input type="text"
                                name="susername"
                                value={susername} ref={this.input}
                                onChange={this.onChange}/>
                            <br/>

                            <label>Password</label><br/>
                            <input type="password"
                                name="spassword"
                                value={spassword} ref={this.input}
                                onChange={this.onChange}/>
                           </form>
                        <button  type="submit"
                        className="btn"
                        onClick={this.signUpToAPI}>Signup</button>
                        </div>
                    </>}
                </div>
            </div> : null }
            </>
        )
    }
}

export default BlockModal;