import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, Alert, Image } from 'react-native';


export default function App() {
  return (
    <View style={styles.container}>
      <StatusBar hidden={true} />
      <Image source={require('./src/images/avatar.png')} style={styles.imageStyle} />
      <Text style={styles.textName}>Rafael Puyau</Text>
      <Text>Data Science</Text>
      <Text>rafael.puyau@gmail.com</Text>
      <View style={styles.containerWP}>
        <Image source={require('./src/images/whatsapp.png')} style={styles.imageWP} />
        <Text>24 99262.1265</Text>
      </View>
      <Button
        title="Message"
        color="#841584"
        onPress={() => Alert.alert('Isto é uma mensagem')}
      />  
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#E7E7E7',
    alignItems: 'center',
    justifyContent: 'center',
  },
  imageStyle: {
    width: 100,
    height: 100,
  },
  textName: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#333333',
    lineHeight: 32,
  },
  containerWP: {
    flexDirection: 'row',
    marginVertical: 10,
  },  
  imageWP: {
    width: 24,
    height: 24,
    marginRight: 8,
  }
});
