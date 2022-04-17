import React from 'react';
import { StyleSheet, View, Text } from 'react-native';

export default function Header(props) {
    return(
        <View style={styles.container}>
            <Text style={styles.headerText}>
                {props.title}
            </Text>
        </View>
    )
}

const styles = StyleSheet.create({
    container: {
        paddingTop: 50,
        paddingBottom: 20,
        backgroundColor: 'navy',
        alignItems: 'center'
    },
    headerText: {
        fontSize: 20,
        fontWeight: 'bold',
        color: '#FFFFFF',
    }
})