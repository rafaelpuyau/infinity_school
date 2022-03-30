import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, Alert, Image } from 'react-native';


export default function App() {
  return (
    <View style={styles.container}>
      <StatusBar hidden={true} />
      <Image source={require('./src/image/avatar.png')} />
      <Image source={{uri: 'https://picsum.photos/200'}} />
      <Text style={styles.text}>Infinity School</Text>
      <View>
        <Text style={styles.texto}>Rafael Puyau</Text>
      </View>
      <View>
        <Text>Data Science</Text>
      </View>
      <View>
        <Text>rafael.puyau@gmail.com</Text>
        <Text style={{ textAlign: 'center' }}>24 99262.1265</Text>
      </View>
      <Button
        title="Press me"
        color="#841584"
        onPress={() => Alert.alert('Minha mensagem')}
      />  
      <Button 
        title="Novo botão"
        onPress={() => Alert.alert('Novo botão funcionando')}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    borderColor: '#777',
    borderStyle: 'solid',
    borderWidth: 20,
    backgroundColor: '#C4C4C4',
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    fontSize: 20,
    color: '#0000FF'
  }
});
