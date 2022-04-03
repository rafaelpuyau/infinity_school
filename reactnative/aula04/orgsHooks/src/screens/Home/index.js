import React from 'react';

import Topo from './components/Topo';
import Produtores from './components/Produtores';

export default function Home(){
    return(
        <>
            {/* <Topo /> // Foi para dentro de Produtores */}
            <Produtores topo={Topo} />
        </>
    )
}