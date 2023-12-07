import React, { Component } from "react"
import { DndProvider } from 'react-dnd'
import { HTML5Backend } from 'react-dnd-html5-backend'
import { Container } from "./Container"

class Dnd extends Component {
  constructor(props) {
    super(props)

    this.state = {}
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
      <>
      {/* https://react-dnd.github.io/react-dnd/examples/dustbin/stress-test */}
        <DndProvider backend={HTML5Backend}>
          <Container />
        </DndProvider>
      </>
    )
  }
}

export default Dnd
