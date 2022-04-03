import React, { useEffect, useState } from 'react';
import { Text, FlatList, StyleSheet } from 'react-native';

import Produtor from './Produtor';
// import { carregaProdutores } from '../../../services/carregaDados';

import useProdutores from '../../../hooks/useProdutores';

export default function Produtores({ topo: Topo }) {
    // Sempre chamar o useState no começo
    // PASSA PARA O MEU HOOK
    // const [titulo, setTitulo] = useState('');
    // const [lista, setLista] = useState([]);


    // LEVO PARA MEU HOOK
    // useEffect(() => {
    //     const retorno = carregaProdutores();
    //     setTitulo(retorno.titulo);
    //     setLista(retorno.lista);
    //     // console.log(retorno)  // Para verificar o retorno
    // }, []);

    const [titulo, lista] = useProdutores();

    const TopoLista = () => {
        return(
            <>
                <Topo />
                <Text style={estilos.titulo}>{ titulo }</Text>
            </>
        )
    }

    return(
        <FlatList
            data={lista}
            keyExtractor={ ( {nome} ) => nome}
            // renderItem={ ({item: { nome }}) => <Text>{ nome }</Text> }
            renderItem={({ item }) => <Produtor {...item}/>}
            ListHeaderComponent={ TopoLista }
        // <Text>{ titulo }</Text> // Passará a ser o Header do FlatList
        />
    )
}

const estilos = StyleSheet.create({
    titulo: {
        fontSize: 20,
        lineHeight: 32,
        marginHorizontal: 16,
        marginTop: 16,
        fontWeight: 'bold',
        color: '#464646',
    }
})