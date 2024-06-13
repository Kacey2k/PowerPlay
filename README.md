# PowerPlay (Indev)
 A statistics utility for TeamFortress 2.
 The end product should track players, maps, servers, messages, and other objects; store them to a client-side database, and provide insight during gameplay.
 
# Architecture Goal
- Configure Client to accept RCon commands & generate console logs for the application.
- Log parser extacts relevant data.
- Session objects generated, defined by current server/map configuration.
- Session controller moves data to appropriate locations, creating new objects if necessary.
- GUI Updates with latest data.
- User manipulates data if desired (E.g., marking a player via GUI).
