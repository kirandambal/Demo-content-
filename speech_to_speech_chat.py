import azure.cognitiveservices.speech as speech_sdk
from openai import AzureOpenAI

ai_key ="66822072569a4e2fa67099063dd346d0"
ai_region ="eastus"
azure_oai_endpoint = "https://azure154815.openai.azure.com/"
azure_oai_key = "66822072569a4e2fa67099063dd346d0"
azure_oai_model = "demo"

# Initialize the Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint = azure_oai_endpoint, 
    api_key=azure_oai_key,  
    api_version="2023-05-15"
        )

def speechrec():
    command = ''

    # Configure speech recognition
    # Configure speech recognition
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)

    while command.lower() != 'quit.':
        print('User :')    
        # Process speech input
        # Process speech input
        speech = speech_recognizer.recognize_once_async().get()
        if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
            command = speech.text
            print(command)
        else:
            print(speech.reason)
            if speech.reason == speech_sdk.ResultReason.Canceled:
                cancellation = speech.cancellation_details
                print(cancellation.reason)
                print(cancellation.error_details)
                
        azopenai(command)

def speechsys(response_text):

    # Configure speech synthesis
    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = 'en-GB-LibbyNeural' # change this
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    # Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

def azopenai(text):

    # Send request to Azure OpenAI model
    response = client.chat.completions.create(
        model=azure_oai_model,
        temperature=0.7,
        max_tokens=120,
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": text}
        ]
    )
    res = response.choices[0].message.content         
    print("\n\nGPT : \n" + res + "\n")
    print("\n##############################################################################")
    speechsys(res)

def main():
    try:
        global speech_config
        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
        print("Hello, Welcome to Speech to speech GPT model:\n\n")
        speechrec()

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()