

// export function DialogBox(
export const DialogBox = ({
  title,
  message,
  textActionA,
  textActionB,
  actionA,
  actionB,
  cancelAction,
  submit
}:{
  title:string, 
  message:string,
  textActionA: string, 
  textActionB: string, 
  actionA: () => void, 
  actionB: () => void,
  cancelAction: () => void,
  submit?: Function
}
) => {

    function handleClick(action: Function) {
      action()
      cancelAction()
      if(submit) submit()
    }
    
    
    console.log('dialogbox')
    // function 
    return(
      <div className='dialog-ovelay'>
        <div className='dialog'>
          <header>
            <h3>{title}</h3>
            <i className='fa fa-close'></i>
          </header>
          <div className='dialog-msg'>
            <p>{message}</p>
          </div>
          <footer>
            <div className='controls'>
              <button className='button button-danger doAction' onClick={() => handleClick(actionA)}>{textActionA}</button>
              <button className='button button-default cancelAction' onClick={() => handleClick(actionB)}>{textActionB}</button>
              <button className='button button-default' onClick={cancelAction}>Cancel</button>
            </div>
          </footer>
        </div>
      </div> 
    )}

//  Example return:
//   return (   
//     <> 
//       <button onClick={() => setSomething(!something)}>Click me</button>
//       {something ? dialogBox(test, mymsg, 'text a', 'text b', action1, action2, myCancel) : ''}
//     </>
//     )