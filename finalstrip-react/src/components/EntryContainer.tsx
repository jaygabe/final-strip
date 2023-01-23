import React, { ReactNode } from 'react'

export const exampleComponent: React.FC<{entry: ReactNode}> = ({entry}) => {
  
    const open = () => {
    alert("You clicked this container component")
    }

  return (
      <>
        {/*<div onClick={open}>*/}
        <div className="container">
            <h1>entry container</h1>
            <img src="../static/edit_icon.svg" alt="edit"  />
	        {entry}
        </div>
    </>
  )
}