# Trading Journal 2026

A trading journal web app with Excel Online integration via Microsoft Graph API.

## Quick Start

### Option 1: Open directly
Open `public/index.html` in your browser.

### Option 2: Run with Flask
```bash
pip install flask
python app.py
```
Then open http://localhost:5000

## Deploy to Vercel

1. Push this repository to GitHub
2. Go to [vercel.com](https://vercel.com) and sign in
3. Click "New Project" and import your GitHub repo
4. Vercel will auto-detect the static site configuration
5. Click "Deploy"

## Connect to Excel Online (Microsoft Graph API)

To enable the "Connect Excel" button that syncs trades with Excel Online on OneDrive:

### Step 1: Register an Azure AD App

1. Go to [Azure Portal](https://portal.azure.com)
2. Navigate to **Azure Active Directory** > **App registrations**
3. Click **New registration**
4. Set the name to `Trading Journal 2026`
5. Under **Redirect URI**, select **Single-page application (SPA)** and enter your Vercel URL (e.g., `https://your-app.vercel.app`)
6. Click **Register**

### Step 2: Configure API Permissions

1. In your app registration, go to **API permissions**
2. Click **Add a permission** > **Microsoft Graph** > **Delegated permissions**
3. Add these permissions:
   - `Files.ReadWrite` (read and write files on OneDrive)
   - `User.Read` (sign in and read user profile)
4. Click **Grant admin consent** (if you're the admin)

### Step 3: Update the Client ID

1. Copy the **Application (client) ID** from the Azure Portal
2. Open `public/index.html`
3. Find the line: `clientId: 'YOUR_CLIENT_ID'`
4. Replace `YOUR_CLIENT_ID` with your actual Client ID

### Step 4: Deploy and Test

1. Push the changes to GitHub
2. Vercel will auto-deploy
3. Open your Vercel URL
4. Click the "Connect Excel" button
5. Sign in with your Microsoft account
6. Use "Sync to Excel" to push trades to Excel Online
7. Use "Load from Excel" to pull trades from Excel Online

## Features

- Import/Export Excel files (local)
- Add, edit, delete trades
- Filter by pair, direction, status, week, setup
- Search trades
- Statistics dashboard
- Drag & drop file import
- Excel Online sync (requires Azure AD setup)
