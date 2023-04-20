import axios from 'axios';
import { useState } from 'react';
import { useParams } from 'react-router-dom';
import { boutType } from '../../constants/VarTypes';
// import { ReactComponent as EditIcon } from "../../static/edit_icon.svg"

export function BoutView() {
  const { slug } = useParams();
  const [dataReceived, setDataReceived] = useState(false);
  const [bout, setBout] = useState<boutType>({
    id: 99,
    slug: '',
    winnerIsA: true,
    fencerA: '',
    fencerB: '',
    scoreA: 0,
    scoreB: 0,
    fencerAHand: '',
    fencerBHand: '',
    fencerAYellowCard: false,
    fencerBYellowCard: false,
    fencerARedCard: false,
    fencerBRedCard: false,
    fencerABlackCard: false,
    fencerBBlackCard: false,
    fencerAPassivity: false,
    fencerBPassivity: false,
    fencerAMedical: false,
    fencerBMedical: false,
    fencerAVideoUsed: 0,
    fencerBVideoUsed: 0,
    fencerAFootwork: '',
    fencerBFootwork: '',
    fencerABladework: '',
    fencerBBladework: '',
    fencerADistance: '',
    fencerBDistance: '',
    fencerATiming: '',
    fencerBTiming: '',
    fencerAEnergy: '',
    fencerBEnergy: '',
    fencerANotes: '',
    fencerBNotes: '',
    referee: '',
    boutFormat: '',
    round: 0,
    notes: '',
    shareCoach: true,
    deleted: false,
  });

  const getData = async () => {
    if (dataReceived === false) {
      const result = await axios.get('api/bouts/detail/' + slug, {
        withCredentials: true,
      });
      console.log('result: ', result.data);
      setDataReceived(true);
      // setBout(result.data)
      setBout({
        id: result.data.id,
        slug: result.data.slug,
        winnerIsA: result.data.winner_is_a,
        fencerA: result.data.fencer_a,
        fencerB: result.data.fencer_b,
        scoreA: result.data.score_a,
        scoreB: result.data.score_b,
        fencerAHand: result.data.fencer__a_hand,
        fencerBHand: result.data.fencer_b_hand,
        fencerAYellowCard: result.data.fencer_a_yellow_card,
        fencerBYellowCard: result.data.fencer_b_yellow_card,
        fencerARedCard: result.data.fencer_a_red_card,
        fencerBRedCard: result.data.fencer_b_red_card,
        fencerABlackCard: result.data.fencer_a_black_card,
        fencerBBlackCard: result.data.fencer_b_black_card,
        fencerAPassivity: result.data.fencer_a_passivity,
        fencerBPassivity: result.data.fencer_b_passivity,
        fencerAMedical: result.data.fencer_a_medical,
        fencerBMedical: result.data.fencer_b_medical,
        fencerAVideoUsed: result.data.fencer_a_video_used,
        fencerBVideoUsed: result.data.fencer_b_video_used,
        fencerAFootwork: result.data.fencer_a_footwork,
        fencerBFootwork: result.data.fencer_b_footwork,
        fencerABladework: result.data.fencer_a_bladework,
        fencerBBladework: result.data.fencer_b_bladework,
        fencerADistance: result.data.fencer_a_distance,
        fencerBDistance: result.data.fencer_b_distance,
        fencerATiming: result.data.fencer_a_timing,
        fencerBTiming: result.data.fencer_b_timing,
        fencerAEnergy: result.data.fencer_a_energy,
        fencerBEnergy: result.data.fencer_b_energy,
        fencerANotes: result.data.fencer_a_notes,
        fencerBNotes: result.data.fencer_b_notes,
        referee: result.data.referee,
        boutFormat: result.data.bout_format,
        round: result.data.round,
        notes: result.data.notes,
        shareCoach: result.data.share_coach,
        deleted: result.data.deleted,
      });
    }
  };
  getData();

  function boutSummaryDetail() {
    return (
      <div className="container">
        <p className="detail">
          {bout.fencerA ? bout.fencerA : 'Unknown'} vs{' '}
          {bout.fencerB ? bout.fencerB : 'Unknown'}
        </p>
        <p className="detail">
          {bout.scoreA} - {bout.scoreB}
        </p>
        {bout.notes ? <p>{bout.notes}</p> : <></>}
      </div>
    );
  }

  function boutOverallDetail() {
    return (
      <section className="bout-tab-content">
        <h2>Overall Data: </h2>
        {bout.referee ? <p>Referee: {bout.referee}</p> : <></>}
        {bout.boutFormat ? <p>Format: {bout.boutFormat}</p> : <></>}
        {bout.round ? <p>Round: {bout.round}</p> : <></>}
        {bout.notes ? <p>Notes: {bout.notes}</p> : <></>}
        {bout.shareCoach ? <p>{bout.shareCoach}</p> : <></>}
      </section>
    );
  }

  function fencerADetail() {
    return (
      <section className="bout-tab-content">
        <h2>Fencer A</h2>
        <h2>Info:</h2>
        {bout.fencerA ? <p>Name: {bout.fencerA}</p> : <></>}
        {bout.scoreA ? <p>Scored: {bout.scoreA}</p> : <></>}
        {bout.fencerAHand ? <p>Handedness: {bout.fencerAHand}</p> : <></>}
        {bout.fencerAPassivity ? (
          <p>Passivity: {bout.fencerAPassivity}</p>
        ) : (
          <></>
        )}
        {bout.fencerAMedical ? (
          <p>Medical time used: {bout.fencerAMedical}</p>
        ) : (
          <></>
        )}
        {bout.fencerAVideoUsed ? (
          <p>Video replays used: {bout.fencerAVideoUsed}</p>
        ) : (
          <></>
        )}
        <h2>Cards:</h2>
        {bout.fencerAYellowCard ? (
          <p>Yellow: {bout.fencerAYellowCard}</p>
        ) : (
          <></>
        )}
        {bout.fencerARedCard ? <p>Red: {bout.fencerARedCard}</p> : <></>}
        {bout.fencerABlackCard ? <p>Black: {bout.fencerABlackCard}</p> : <></>}
        <h2>Fencer Ratings:</h2>
        {bout.fencerAFootwork ? <p>Footwork: {bout.fencerAFootwork}</p> : <></>}
        {bout.fencerABladework ? (
          <p>Bladework: {bout.fencerABladework}</p>
        ) : (
          <></>
        )}
        {bout.fencerATiming ? <p>Timing: {bout.fencerATiming}</p> : <></>}
        {bout.fencerAEnergy ? <p>Energy: {bout.fencerAEnergy}</p> : <></>}
        {bout.fencerANotes ? <p>Notes: {bout.fencerANotes}</p> : <></>}
      </section>
    );
  }

  function fencerBDetail() {
    return (
      <section className="bout-tab-content">
        <h2>Fencer B</h2>
        <h2>Info:</h2>
        {bout.fencerB ? <p>Name: {bout.fencerB}</p> : <></>}
        {bout.scoreB ? <p>Scored: {bout.scoreB}</p> : <></>}
        {bout.fencerBHand ? <p>Handedness: {bout.fencerBHand}</p> : <></>}
        {bout.fencerBPassivity ? (
          <p>Passivity: {bout.fencerBPassivity}</p>
        ) : (
          <></>
        )}
        {bout.fencerBMedical ? <p>Medical: {bout.fencerBMedical}</p> : <></>}
        {bout.fencerBVideoUsed ? <p>Video: {bout.fencerBVideoUsed}</p> : <></>}
        <h2>Cards:</h2>
        {bout.fencerBYellowCard ? (
          <p>Yellow: {bout.fencerBYellowCard}</p>
        ) : (
          <></>
        )}
        {bout.fencerBRedCard ? <p>Red: {bout.fencerBRedCard}</p> : <></>}
        {bout.fencerBBlackCard ? <p>Black: {bout.fencerBBlackCard}</p> : <></>}
        <h2>Fencer Ratings:</h2>
        {bout.fencerBFootwork ? <p>Footwork: {bout.fencerBFootwork}</p> : <></>}
        {bout.fencerBBladework ? (
          <p>Bladework: {bout.fencerBBladework}</p>
        ) : (
          <></>
        )}
        {bout.fencerBTiming ? <p>Timing: {bout.fencerBTiming}</p> : <></>}
        {bout.fencerBEnergy ? <p>Energy: {bout.fencerBEnergy}</p> : <></>}
        {bout.fencerBNotes ? <p>Notes: {bout.fencerBNotes}</p> : <></>}
      </section>
    );
  }

  return (
    <>
      {boutSummaryDetail()}

      <div className="container">
        <div className="bout-tabs">
          <input
            className="bout-tab-radio"
            type="radio"
            id="overall"
            name="bout-info"
            defaultChecked
          />
          {/* <label className='bout-tab-radio' htmlFor="overall"><EditIcon/><br/><span>Overall</span></label> */}
          {boutOverallDetail()}

          <input
            className="bout-tab-radio"
            type="radio"
            id="fencer-a"
            name="bout-info"
          />
          {/* <label className='bout-tab-radio' htmlFor="fencer-a"><EditIcon/><br/><span>Fencer A</span></label> */}
          {fencerADetail()}

          <input
            className="bout-tab-radio"
            type="radio"
            id="fencer-b"
            name="bout-info"
          />
          {/* <label className='bout-tab-radio' htmlFor="fencer-b"><EditIcon/><br/><span>Fencer B</span></label> */}
          {fencerBDetail()}
        </div>
      </div>
    </>
  );
}
