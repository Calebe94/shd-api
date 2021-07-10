#This file is part of the SHD distribution (https://gitlab.com/projeto-leitor-hidrometro).
#Copyright (C) 2021 TinyTools
#
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

from typing import List, Optional

from pydantic import BaseModel


class LeituraBase(BaseModel):
    device: int
    leitura: float
    timestamp: int


class LeituraCreate(LeituraBase):
    pass


class Leitura(LeituraBase):
    id: int

    class Config:
        orm_mode = True
