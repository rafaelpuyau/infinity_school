import React from 'react';
import { StyleSheet, View, Text } from 'react-native';


export default function MeuComponente(){
    return(
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Infinity School</Text>
        <Text style={styles.cardText}>Criando aplicações mobile para Android e iOS</Text>
      </View>
    )
}

const styles = StyleSheet.create({
    card: {
      backgroundColor: '#F4EBDF',
      padding: 12,
      borderRadius: 3,
      marginVertical: 7
    },
    cardTitle: {
      fontSize: 18,
      fontWeight: 'bold'
    },
    cardText: {
      color: '#777777',
      fontSize: 14
    }
  });