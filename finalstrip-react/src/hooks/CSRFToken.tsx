import { useEffect } from "react";
import axios from "axios";

export const CSRFToken = () => {
    useEffect(() => {
        axios.get('api/auth/csrf-token', {
                headers: { 'Authorization': '' },
                withCredentials: true,
            }
        ).catch( () => {
            alert('Error message.');
        });
    }, []);

    return <></>
}
