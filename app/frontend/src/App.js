import React, { Component } from "react"

import Dnd from "./DnD"

class App extends Component {
  constructor(props) {
    super(props)

    this.state = {
      nakejtext: "zatim nic",
    }
  }

  componentDidMount() {
    console.log("componentDidMount")
  }

  getText() {
    fetch("https://jsonplaceholder.typicode.com/todos/1")
      .then((result) => result.json())
      .then((result) => {
        this.setState({
          nakejtext: result.title,
        })
      })
  }

  render() {
    return (
      <div>
        <div>{this.state.nakejtext}</div>
        <button onClick={() => this.getText()}>Get text</button>
        <br />
        <Dnd />
      </div>
    )
  }
}

export default App
