#include<iostream>
#include<string>
using namespace std;
const int people = 4;//�����������
int lefts[people+1];//����������
int rights[people+1];//�����Ҳ����
int speed[people + 1];//ÿ���˵��ٶ�
int m_T;//��¼���ٻ���ʱ��
int P_P[4];
void init() {
	int i, j, k;
	cout << "������" << people << "���˵��ٶ�" << endl;
	for (i = 1; i <= people; i++)
	{
		rights[i] = 0;
		lefts[i] = 1;
		cin >> speed[i];
	}
	for (j = 1; j <= 4; j++)
		P_P[j] = 0;
	
}
int end()
{
	for (int i = 1; i < people; i++)
	{
		if (rights[i] == 0)
		{
			return 1;
		}
	}
	return 0;
}
void judge(int lm1, int lm2, int lo1, int lo2)//�ٶ�lo2>lo1>lm2>lm1
{
	int lmin1 = speed[lm1], lmin2 = speed[lm2], long1 = speed[lo1], long2 = speed[lo2];
	if (2 * lmin2 > lmin1 + long1)
		m_T += lmin1 * 2 + lmin2 + long1 + long2;
	else
		m_T += lmin1 + 3 * lmin2 + long2;
	if (end())
	{
		lefts[lm1] = 1;
		rights[lm1] = 0;
		m_T += speed[lm1];
	}
	else {
		cout << "��С��ʱΪ" << m_T<<endl;
	}
}
void Pass_Person()
{
	int i, j, k;
	int min=10000, max=0,tot1=0,tot2=0;
	for (i = 1; i <= people; i++)
	{
		if (lefts[i] == 1)
		{
			if (speed[i] < min)
			{
				min = speed[i];
				tot1 = i;
			}
			if (speed[i] > max)
			{
				max = speed[i];
				tot2 = i;
			}
		}
	}
	lefts[tot1] = lefts[tot2] = 0;
	rights[tot1] = rights[tot2] = 1;
	P_P[0] = tot1;
	P_P[3] = tot2;
	min = 10000, max = 0;
	for (i = 1; i <= people; i++)
	{
		if (lefts[i] == 1)
		{
			if (speed[i] < min)
			{
				min = speed[i];
				tot1 = i;
			}
			if (speed[i] > max)
			{
				max = speed[i];
				tot2 = i;
			}
		}
	}
	lefts[tot1] = lefts[tot2] = 0;
	rights[tot1] = rights[tot2] = 1;
	P_P[1] = tot1;
	P_P[2] = tot2;
	judge(P_P[0], P_P[1], P_P[2], P_P[3]);
} 
void main()
{
	init();
	while (end())
	{
		Pass_Person();
	}
	system("pause");
}