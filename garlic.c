#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
	printf("гайд как закачать чеснок на комп\n");
	sleep(1.5);
	system("xdg-open https://dvemorkovki.ru/upload/iblock/109/b679m89gzu9q4692lrgmobc23vizzl98/304232_5.jpg 2> /dev/null &");
	sleep(3.5);
	printf("скачка чеснока...\n");
	system("mpv ожидание.mp3 &");
	system("curl -s -o 'chesnoeb.png' 'https://i.imgur.com/zWphWZ6.png'");
	system("curl -s -o 'music.mp3' 'https://ia601209.us.archive.org/1/items/OMFGHello_20150908/OMFG%20-%20Hello.mp3'");
	system("pkill mpv");
	system("mpv music.mp3 &");
	do {
		sleep(1.5);
		system("feh -F chesnoeb.png &");
	} while(1);

	return 0;
}
