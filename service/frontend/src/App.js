import './App.css';
import React from 'react';
import axios from 'axios';
import AuthorList from './components/Author.js'
import Footer from './components/Footer.js'
import Menu from "./components/Menu.js";


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'authors': []
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/authors/')
            .then(response => {
                const authors = response.data.results
                    this.setState(
                    {
                        'authors': authors
                    }
                )
            }).catch(error => console.log(error))
    }

    render () {
        return (
            <div>
                <Menu />
                <AuthorList authors={this.state.authors} />
                <Footer />
            </div>
        )
    }
}

export default App;


//function App() {
//  return (
//    <div className="App">
//      <header className="App-header">
//        <img src={logo} className="App-logo" alt="logo" />
//        <p>
//          Edit <code>src/App.js</code> and save to reload.
//        </p>
//        <a
//          className="App-link"
//          href="https://reactjs.org"
//          target="_blank"
//          rel="noopener noreferrer"
//        >
//          Learn React
//        </a>
//      </header>
//    </div>
//  );
//}
//
//export default App;
