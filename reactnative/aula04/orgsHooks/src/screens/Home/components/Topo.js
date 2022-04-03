import React, { Component } from 'react';
import { View, Text, Image, StyleSheet } from 'react-native';

import { carregaTopo } from '../../../services/carregaDados';

import logo from '../../../assets/logo.png';
// import topo from '../../../mocks/topo';

// export default function Topo() {
//     return(
//         <View style={estilos.topo}>
//             <Image source={logo} style={estilos.imagem}/>
//             <Text style={estilos.boasVindas}>Olá Rafael</Text>
//             <Text style={estilos.legenda}>Encontre os melhores produtores</Text>
//         </View>
//     )
// }

class Topo extends Component {

    // Criando os estados
    state = {
        topo: {
            boasVindas: '',
            legenda: '',
        },
    }

    atualizaTopo() {
        const retorno = carregaTopo();
        this.setState({ topo: retorno })
    }

    componentDidMount() {
        this.atualizaTopo();
    }

    render() {
        return(
            <View style={estilos.topo}>
                <Image source={logo} style={estilos.imagem} />
                <Text style={estilos.boasVindas}>{ this.state.topo.boasVindas }</Text>
                <Text style={estilos.legenda}>{ this.state.topo.legenda }</Text>
            </View>
        )
    }
}

const estilos = StyleSheet.create({
    topo: {
        backgroundColor: '#F6F6F6',
        padding: 16,
    },
    imagem: {
        width: 70,
        height: 28,
    },
    boasVindas: {
        marginTop: 24,
        fontSize: 26,
        lineHeight: 42,
        fontWeight: 'bold',
        color: '#464646',
    },
    legenda: {
        fontSize: 16,
        lineHeight: 26,
        color: '#A3A3A3',
    }
})

export default Topo;