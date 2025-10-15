# Banking App - Mobile (React Native)

Native mobile application built with React Native and Expo.

## Features

- **Native Experience**: Smooth animations and native UI components
- **Biometric Auth**: Fingerprint and Face ID support
- **Push Notifications**: Real-time alerts for transactions
- **Offline Mode**: View cached data when offline
- **Cross-platform**: Runs on iOS and Android
- **All Web Features**: Complete feature parity with web app

## Tech Stack

- React Native (Expo)
- TypeScript
- React Native Paper (UI components)
- React Navigation
- Firebase Auth
- Expo modules (biometrics, secure storage, notifications)

## Setup

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Install Expo CLI** (if not already installed):
   ```bash
   npm install -g expo-cli
   ```

3. **Configure app.json**:
   Update Firebase configuration

4. **Run development server**:
   ```bash
   npm start
   ```

   Then:
   - Press `i` for iOS simulator
   - Press `a` for Android emulator
   - Scan QR code with Expo Go app on your phone

## Project Structure

```
src/
├── screens/         # App screens
├── components/      # Reusable components
├── navigation/      # Navigation configuration
├── services/        # API services
├── hooks/           # Custom hooks
├── utils/           # Utility functions
└── types/           # TypeScript types
```

## Key Features

### Biometric Authentication
Uses Expo Local Authentication for fingerprint/Face ID login

### Push Notifications
Real-time notifications for:
- Large transactions
- Budget alerts
- Goal achievements
- Unusual activity

### Offline Support
Caches account and transaction data for offline viewing

## Building for Production

### iOS
```bash
expo build:ios
```

### Android
```bash
expo build:android
```

## License

MIT

