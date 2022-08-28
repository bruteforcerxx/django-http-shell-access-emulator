import { dispatchEvent } from '../helpers/events';
const evalCommand = (cmd, instance) => {
    const { print } = instance;
    const splitCommand = cmd.split(' ');
    const command = splitCommand[0];
    const commandArguments = splitCommand.slice(1);
    const commandInstance = instance.settings.commands[command];
    if (commandInstance) {
        if (commandInstance.argDescriptions &&
            commandInstance.argDescriptions.length > 0 &&
            commandArguments.length === 0) {
            print(`Usage: ${command} ${commandInstance
                .argDescriptions.map(arg => `[${arg}]`).join(' ')}`);
        }
        else {
            commandInstance.func(instance, ...commandArguments);
            dispatchEvent("onCommand" /* ON_COMMAND */, instance.settings.host, cmd);
        }
    }
    else {
        print(`<span class="terminal-error">command not found: ${command}</span>`);
        dispatchEvent("onCommand404" /* ON_COMMAND_NOT_FOUND */, instance.settings.host, cmd);
    }
};
export default evalCommand;
