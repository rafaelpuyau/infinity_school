import { StatusBar } from 'expo-status-bar';
import React, { useState } from 'react';
import { 
  StyleSheet, 
  Text, 
  TextInput, 
  View, 
  Button, 
  Alert 
} from 'react-native';


export default function App() {

  const [name, setName] = useState("---");
  const [age, setAge] = useState("---");
  
  return (
    <View style={styles.container}>
      <Text>Validando informações no campo</Text>
      <StatusBar style="auto" />

      <TextInput
        style={styles.input}
        placeholder="e.g. your name"
        onChangeText={(val) => setName(val)}
        />

      <TextInput
        style={styles.input}
        keyboardType='numeric'
        placeholder="e.g. your age"
        onChangeText={(val) => setAge(val)}
        />

        <Text>Name: {name}</Text>
        <Text>Age: {age}</Text>
      

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  input: {
    height: 40,
    width: 250,
    borderWidth: 1,
    borderRadius: 3,
    padding: 10,
    margin: 12
  },
});

