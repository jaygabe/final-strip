// import CSS from 'csstype'
// import { useState } from 'react';
// import { FormRatingElement } from '../components/forms/form elements/FormRatingElement';
// import { FormTextElement } from '../components/forms/form elements/FormTextElement';
import { FormNumberElement } from '../components/forms/form_elements/FormNumberElement';
import { DialogBox } from '../components/DialogBox';

import { useState, SyntheticEvent } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

export function Test() {
  // const [rating, setRating] = useState<number | null>(0);
  // // const [hover, setHover] = useState(0);
  // const [something, setSomething] = useState(false)

  // const test = 'title'
  // const mymsg = 'message'
  // function action1() {console.log('action1')}
  // function action2() {console.log('action2')}
  // function myCancel() {setSomething(false)}

  // function handleClick(e: React.MouseEvent<HTMLButtonElement>){
  //   if (rating === null || rating >= 2 ){

  //     setSomething(!something)
  //   }
  // }

  // function DialogBox(
  //   title:string,
  //   msg:string,
  //   textActionA: string,
  //   textActionB: string,
  //   actionA: void | (() => void),
  //   actionB: void | (() => void),
  //   cancelButton?: void | (() => void)
  //   ){
  //   return(
  //     <div className='dialog-ovelay'>
  //       <div className='dialog'>
  //         <header>
  //           <h3>{title}</h3>
  //           <i className='fa fa-close'></i>
  //         </header>
  //         <div className='dialog-msg'>
  //           <p>{msg}</p>
  //         </div>
  //         <footer>
  //           <div className='controls'>
  //             <button className='button button-danger doAction' onClick={() => actionA}>{textActionA}</button>
  //             <button className='button button-default cancelAction' onClick={() => actionB}>{textActionB}</button>
  //             {cancelButton
  //               ? <button className='button button-default' onClick={cancelButton}>Cancel</button>
  //               : ''}
  //           </div>
  //         </footer>
  //       </div>
  //     </div>
  //   )}

  // return(
  //   <>
  //     <FormNumberElement setValue={setRating} labelText='Rating' elementName='rating' />
  //     <button onClick={e => handleClick(e)}>Click me</button>
  //     {something ? DialogBox(test, mymsg, 'text a', 'text b', action1, action2, myCancel) : ''}
  //   </>
  //   )

  const { eventSlug } = useParams();
  const [winnerIsA, setWinnerIsA] = useState<null | boolean>(null);
  const [scoreA, setScoreA] = useState<number | null>(null);
  const [scoreB, setScoreB] = useState<number | null>(null);

  // const [showDialogBox, setShowDialogBox] = useState(false)
  let showDialogBox = false;
  function setShowDialogBox(value: boolean) {
    showDialogBox = value;
  }

  // process form before submitting
  const handleClick = (e: SyntheticEvent) => {
    // e.preventDefault()
    if (scoreA == null || scoreB == null) {
      alert('score is required');
      return;
    }
    // assign winner
    if (scoreA > scoreB) {
      setWinnerIsA(true);
    }
    if (scoreA < scoreB) {
      setWinnerIsA(false);
    }
    // if score is tied, show dialog box to choose a winner
    if (scoreA == scoreB && winnerIsA === null) {
      setShowDialogBox(true);
      console.log('showDialogBox: ', showDialogBox);
      return;
    }

    console.log('sending data to backend...');
    async function sendData() {
      const { data } = await axios.post(
        'api/events/create/',
        {
          event_slug: eventSlug,
          score_a: scoreA,
          score_b: scoreB,
          winner_is_a: winnerIsA,
        },
        { withCredentials: true }
      );
    }
    sendData();
  };

  return (
    <>
      {/* {showDialogBox ? DialogBox(
                'Tied Score', 
                'Please select a winner.', 
                'Fencer A', 
                'Fencer B', 
                setWinnerIsA(true), 
                setWinnerIsA(false), 
                setShowDialogBox(false)) 
            : ''} */}

      <form>
        <h1 className="h1">New Game</h1>
        <FormNumberElement
          setValue={setScoreA}
          elementName="score-a"
          labelText="Score A"
        />
        <FormNumberElement
          setValue={setScoreB}
          elementName="score-b"
          labelText="Score B"
        />
        <button
          className="submit-button"
          type="button"
          onClick={(e) => handleClick(e)}
        >
          Add Bout
        </button>
        <button type="button" onClick={() => setWinnerIsA(null)}>
          reset winner_is_a
        </button>
      </form>
    </>
  );
}
